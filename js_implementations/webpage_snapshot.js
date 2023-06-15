const puppeteer = require("puppeteer");
const fs = require("fs");
const url = process.argv[2];

(async () => {
    const browser = await puppeteer.launch({args: ["--no-sandbox"], headless: "new"});
    const page = await browser.newPage();
    await page.goto(url);
    await page.screenshot({path: "/home/chatgpt/custom_utilities/utility_library/tmp/screenshot.png"});
    await browser.close();
})();
