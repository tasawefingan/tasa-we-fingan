# Migration Guide: Static HTML to Google Sheets Database

This guide explains how to set up your Google Sheet and Google Apps Script to serve as the JSON database for your refactored website.

## 1. Google Sheet Structure

Create a new Google Sheet and rename the first tab to `Menu`.
Create the following exact column headers in row 1:

| id | category_ar | category_en | name_ar | name_en | description_ar | description_en | price | image_url | availability | display_order |
|----|-------------|-------------|---------|---------|----------------|----------------|-------|-----------|--------------|---------------|

*Fill your menu items starting from row 2.*
- **availability**: Set to `TRUE` or `FALSE` (if FALSE, the item won't show on the website).
- **display_order**: Use numbers (1, 2, 3...) to control the order of items and categories.

## 2. Google Apps Script Setup

1. In your Google Sheet, go to **Extensions > Apps Script**.
2. Delete any existing code in the editor and paste the following code:

```javascript
function doGet(e) {
  const sheetName = 'Menu';
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sheetName);
  
  if (!sheet) {
    return ContentService.createTextOutput(JSON.stringify({error: "Sheet 'Menu' not found"}))
      .setMimeType(ContentService.MimeType.JSON);
  }
  
  const data = sheet.getDataRange().getValues();
  const headers = data[0];
  const rows = data.slice(1);
  
  const result = rows.map(row => {
    let obj = {};
    headers.forEach((header, index) => {
      obj[header] = row[index];
    });
    return obj;
  });
  
  // Return JSON output with CORS headers
  return ContentService.createTextOutput(JSON.stringify(result))
    .setMimeType(ContentService.MimeType.JSON);
}
```

3. Click the **Save** icon.
4. Click **Deploy > New deployment**.
5. Select type: **Web app**.
6. Set "Execute as" to **Me**.
7. Set "Who has access" to **Anyone**.
8. Click **Deploy**. (You will be prompted to authorize the script; follow the steps).
9. Copy the **Web app URL**.

## 3. Update Frontend Config

1. Open `config.js` in your website files.
2. Replace the `API_URL` value with the new Web app URL you just copied.
3. Save the file.

## 4. GitHub Pages Deployment

Since this project now consists entirely of vanilla HTML, CSS, and JS (`index.html`, `style.css`, `app.js`, `config.js`), you can directly commit all changes and push them to your GitHub repository.
GitHub Pages will serve these static files instantly, and the `app.js` will fetch your live data from the Google Apps Script URL seamlessly using Stale-While-Revalidate caching!
