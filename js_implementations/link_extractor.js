const puppeteer = require('puppeteer');
const fs = require('fs');
const util = require('util');

const writeFile = util.promisify(fs.writeFile);

async function linkExtractor(url) {
  const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
  const page = await browser.newPage();
  await page.goto(url, {waitUntil: 'networkidle2'});

  const links = await page.eval('a', as => as.map(a => a.href));

  await writeFile('/home/chatgpt/custom_utilities/utility_library/tmp/links.txt', links.join('\n'));

  await browser.close();
}

linkExtractor(process.argv[2]).catch(err => console.error(err));
