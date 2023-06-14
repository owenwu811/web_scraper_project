const puppeteer = require('puppeteer');
const fetch = require('node-fetch');
const fs = require('fs');

async function downloadFile(url) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url);

    // Get the href attribute of the download link
    const downloadLink = await page.evaluate(() => {
        // This selector should target the download link
        const link = document.querySelector('a[href$=".xls"], a[href$=".xlsx"], a[href$=".csv"]');
        return link.href;
    });

    // Use the node-fetch library to download the file
    const response = await fetch(downloadLink);
    const buffer = await response.buffer();
    fs.writeFile('/path/to/save/file.xls', buffer, () => {
        console.log('Finished downloading file.');
    });

    await browser.close();
}

// Get the URL from the command-line arguments
const url = process.argv[2];
if (!url) {
    console.log('Please provide a URL as a command-line argument.');
    process.exit(1);
}

downloadFile(url);
