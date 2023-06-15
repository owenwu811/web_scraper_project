const puppeteer = require('puppeteer');
const fs = require('fs');
const util = require('util');

const writeFile = util.promisify(fs.writeFile);

async function contentFilter(url, keyword) {
  console.log('Launching browser...');
  const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
  console.log('Browser launched.');

  console.log('Opening new page...');
  const page = await browser.newPage();
  console.log('New page opened.');

  console.log('Navigating to URL...');
  await page.goto(url, {waitUntil: 'networkidle2'});
  console.log('Navigation complete.');

  console.log('Extracting content...');
  const content = await page.eval('*', elements => elements.map(el => el.textContent));
  console.log('Content extracted.');

  console.log('Filtering content...');
  const filteredContent = content.filter(text => text.includes(keyword));
  console.log('Content filtered.');

  console.log('Writing to file...');
  await writeFile('/home/chatgpt/custom_utilities/utility_library/tmp/filtered_content.txt', filteredContent.join('\n'));
  console.log('File written.');

  console.log('Closing browser...');
  await browser.close();
  console.log('Browser closed.');
}

contentFilter(process.argv[2], process.argv[3]).catch(err => console.error(err));
