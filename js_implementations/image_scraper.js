const puppeteer = require("puppeteer");
const fs = require("fs");
const path = require("path");
const url = process.argv[2];
const downloadPath = "/home/chatgpt/custom_utilities/utility_library/tmp";

(async () => {
    const browser = await puppeteer.launch({args: ["--no-sandbox"]});
    const page = await browser.newPage();
    await page.goto(url);

    const imgLinks = await page.evaluate(() => {
        return Array.from(document.images, img => img.src);
    });

    for (let i = 0; i < imgLinks.length; i++) {
        const viewSource = await page.goto(imgLinks[i]);
        fs.writeFile(path.join(downloadPath, `image${i}.jpg`), await viewSource.buffer(), function(err) {
            if(err) {
                return console.log(err);
            }
            console.log("The file was saved!");
        });
    }

    await browser.close();
})();
