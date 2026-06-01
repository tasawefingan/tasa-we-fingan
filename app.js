class MenuApp {
  constructor() {
    this.currentLang = CONFIG.DEFAULT_LANG || 'ar';
    this.menuData = [];

    // DOM Elements
    this.container = document.getElementById('menu-container');
    this.langBtn = document.querySelector('.lang-switch button');

    // Intersection Observer for scroll animations
    this.observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          obs.unobserve(entry.target);
        }
      });
    }, { root: null, rootMargin: '0px', threshold: 0.1 });

    this.init();
  }

  async init() {
    this.setupEventListeners();
    this.setupFeedbackForm();

    // 1. Render immediately from cache if available (Stale)
    this.loadFromCache();

    // 2. Fetch fresh data from API (Revalidate)
    await this.fetchData();

    // 3. Start auto-refresh interval
    setInterval(() => this.fetchData(true), CONFIG.REFRESH_INTERVAL);
  }

  setupEventListeners() {
    if (this.langBtn) {
      this.langBtn.addEventListener('click', () => this.toggleLanguage());
    }
  }

  loadFromCache() {
    const cached = localStorage.getItem(CONFIG.CACHE_KEY);
    if (cached) {
      try {
        const data = JSON.parse(cached);
        if (Array.isArray(data) && data.length > 0) {
          this.menuData = data;
          this.render();
        }
      } catch (e) {
        console.error('Error parsing cache:', e);
      }
    }
  }

  async fetchData(silent = false) {
    try {
      const response = await fetch(CONFIG.API_URL);
      if (!response.ok) throw new Error('Network response was not ok');
      const result = await response.json();
      const data = result.data || [];

      // Check if data actually changed to prevent unnecessary re-renders (no flickering)
      const newDataString = JSON.stringify(data);
      const oldDataString = localStorage.getItem(CONFIG.CACHE_KEY);

      if (newDataString !== oldDataString) {
        localStorage.setItem(CONFIG.CACHE_KEY, newDataString);
        this.menuData = data;
        this.render();
      }
    } catch (error) {
      console.error('Error fetching fresh data:', error);
      // If fetching fails, we just rely on cache.
    }
  }

  groupDataByCategory() {
    const grouped = {};

    // Filter available items and sort by display_order
    const activeItems = this.menuData
      .filter(item => item.availability !== false && item.availability !== 'FALSE')
      .sort((a, b) => {
        const orderA = a.display_order || a.order || 0;
        const orderB = b.display_order || b.order || 0;
        return orderA - orderB;
      });

    activeItems.forEach(item => {
      const catAr = item.category_ar || 'أخرى';
      const catEn = item.category_en || 'Other';

      // We'll use the arabic name as the key for grouping
      if (!grouped[catAr]) {
        grouped[catAr] = {
          ar: catAr,
          en: catEn,
          items: []
        };
      }
      grouped[catAr].items.push(item);
    });

    return grouped;
  }

  render() {
    if (!this.container) return;

    // Clear container
    this.container.innerHTML = '';

    const groupedData = this.groupDataByCategory();

    Object.values(groupedData).forEach(category => {
      // Create section
      const section = document.createElement('section');

      // Title
      const title = document.createElement('h2');
      title.setAttribute('data-ar', category.ar);
      title.setAttribute('data-en', category.en);
      title.textContent = this.currentLang === 'ar' ? category.ar : category.en;
      section.appendChild(title);

      // Note (If the first item has a description, we can treat it as a category note for backward compatibility if needed, but let's just stick to the prompt's per-item description or render it if present)
      // Check if there is a common note we can extract (Optional enhancement based on old design)

      const grid = document.createElement('div');
      grid.className = 'menu-grid';

      // Group items into cards (old design had ~3-5 items per card)
      // For responsiveness, we can put items in a single card or split them.
      // Let's create one card per category, CSS grid will handle it.
      const card = document.createElement('div');
      card.className = 'menu-card';

      category.items.forEach(item => {
        const menuItem = document.createElement('div');
        menuItem.className = 'menu-item';

        const nameSpan = document.createElement('span');
        nameSpan.setAttribute('data-ar', item.name_ar || '');
        nameSpan.setAttribute('data-en', item.name_en || '');
        nameSpan.textContent = this.currentLang === 'ar' ? (item.name_ar || '') : (item.name_en || '');

        // If there is an item description, we can append it as a smaller text
        if (item.description_ar || item.description_en) {
          const desc = document.createElement('div');
          desc.style.fontSize = '12px';
          desc.style.color = 'var(--text-muted)';
          desc.setAttribute('data-ar', item.description_ar || '');
          desc.setAttribute('data-en', item.description_en || '');
          desc.textContent = this.currentLang === 'ar' ? (item.description_ar || '') : (item.description_en || '');
          nameSpan.appendChild(document.createElement('br'));
          nameSpan.appendChild(desc);
        }

        const priceSpan = document.createElement('span');
        priceSpan.className = 'price';
        priceSpan.textContent = item.price;

        menuItem.appendChild(nameSpan);
        menuItem.appendChild(priceSpan);

        card.appendChild(menuItem);
      });

      grid.appendChild(card);
      section.appendChild(grid);

      this.container.appendChild(section);
      this.observer.observe(section);
    });

    // Also observe the static footer and feedback form if they exist
    document.querySelectorAll('.feedback-cute-force, .footer').forEach(el => {
      this.observer.observe(el);
    });
  }

  toggleLanguage() {
    const html = document.documentElement;
    this.currentLang = this.currentLang === 'ar' ? 'en' : 'ar';

    if (this.currentLang === 'en') {
      html.setAttribute('dir', 'ltr');
      html.setAttribute('lang', 'en');
      if (this.langBtn) this.langBtn.textContent = 'AR';
    } else {
      html.setAttribute('dir', 'rtl');
      html.setAttribute('lang', 'ar');
      if (this.langBtn) this.langBtn.textContent = 'EN';
    }

    // Update DOM text based on data attributes
    const textElements = document.querySelectorAll('[data-ar]');
    textElements.forEach(el => {
      const text = el.getAttribute(`data-${this.currentLang}`);
      if (text) {
        // Only replace text nodes to preserve child elements like <br>
        Array.from(el.childNodes).forEach(node => {
          if (node.nodeType === Node.TEXT_NODE && node.textContent.trim() !== '') {
            // For simple elements without complex HTML, direct textContent replacement works.
            // But since we appended desc as child, we should re-render or just use data attributes carefully.
            // Actually, re-rendering the whole menu is cleaner and guarantees consistency!
          }
        });
      }
    });

    // Re-render the menu to apply translations cleanly
    this.render();

    // Update placeholders for feedback form
    const placeholderElements = document.querySelectorAll('input[data-ar-placeholder], textarea[data-ar-placeholder]');
    placeholderElements.forEach(el => {
      el.placeholder = el.getAttribute(`data-${this.currentLang}-placeholder`) || '';
    });
  }

  setupFeedbackForm() {
    const form = document.getElementById('contact-form');
    const status = document.getElementById('form-status');

    if (form && status) {
      form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const data = new FormData(form);

        try {
          const response = await fetch(form.action, {
            method: form.method,
            body: data,
            headers: { Accept: 'application/json' }
          });

          if (response.ok) {
            status.textContent = this.currentLang === 'ar' ? '✅ شكرًا ليك! تم إرسال رسالتك بنجاح.' : '✅ Thank you! Your message has been sent successfully.';
            status.style.color = '#4ade80';
            form.reset();
          } else {
            status.textContent = this.currentLang === 'ar' ? '❌ حصل خطأ، حاول مرة تانية.' : '❌ An error occurred, please try again.';
            status.style.color = '#f87171';
          }
        } catch {
          status.textContent = this.currentLang === 'ar' ? '❌ حصل خطأ، حاول مرة تانية.' : '❌ An error occurred, please try again.';
          status.style.color = '#f87171';
        }
      });
    }
  }
}

// Initialize the app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  window.app = new MenuApp();
});
