const puppeteer = require("puppeteer");
const fs = require("fs");
const url = process.argv[2];

(async () => {
    const browser = await puppeteer.launch({args: ["--no-sandbox"], headless: "new"});
    const page = await browser.newPage();
    await page.goto(url);

    const links = await page.evaluate(() => {
        return Array.from(document.querySelectorAll("a"), a => a.href);
    });

    const sitemap = {};
    for (let link of links) {
        if (link.startsWith(url)) {
            sitemap[link] = [];
        }
    }

    for (let link of Object.keys(sitemap)) {
        await page.goto(link);
        const subLinks = await page.evaluate(() => {
            return Array.from(document.querySelectorAll("a"), a => a.href);
        });
        for (let subLink of subLinks) {
            if (subLink.startsWith(url)) {
                sitemap[link].push(subLink);
            }
        }
    }

    fs.writeFile("/home/chatgpt/custom_utilities/utility_library/tmp/sitemap.json", JSON.stringify(sitemap, null, 2), err => {
        if (err) {
            console.error(err);
            return;
        }
    });

    await browser.close();
})();
