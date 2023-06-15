const puppeteer = require("puppeteer");
const fs = require("fs");
const url = process.argv[2];

(async () => {
    const browser = await puppeteer.launch({args: ["--no-sandbox"], headless: "new"});
    const page = await browser.newPage();
    await page.goto(url);

    await page.evaluate(async () => {
        await new Promise((resolve, reject) => {
            var totalHeight = 0;
            var distance = 100;
            var timer = setInterval(() => {
                var scrollHeight = document.body.scrollHeight;
                window.scrollBy(0, distance);
                totalHeight += distance;

                if (totalHeight >= scrollHeight){
                    clearInterval(timer);
                    resolve();
                }
            }, 100);
        });
    });

    await page.screenshot({path: "/home/chatgpt/custom_utilities/utility_library/tmp/scroll_simulator.png"});
    await browser.close();
})();
