const puppeteer = require('puppeteer');
const fs = require('fs');
const util = require('util');

const writeFile = util.promisify(fs.writeFile);

async function loginManager(url) {
  const username = process.env.USERNAME;
  const password = process.env.PASSWORD;

  console.log('Launching browser...');
  const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
  console.log('Browser launched.');

  console.log('Opening new page...');
  const page = await browser.newPage();
  console.log('New page opened.');

  console.log('Navigating to URL...');
  await page.goto(url, {waitUntil: 'networkidle2'});
  console.log('Navigation complete.');

  console.log('Logging in...');
  await page.type('#username', username);
  await page.type('#password', password);
  await page.click('#login');
  await page.waitForNavigation();
  console.log('Logged in.');

  console.log('Writing cookies to file...');
  const cookies = await page.cookies();
  await writeFile('/home/chatgpt/custom_utilities/utility_library/tmp/cookies.txt', JSON.stringify(cookies));
  console.log('Cookies written.');

  console.log('Closing browser...');
  await browser.close();
  console.log('Browser closed.');
}

loginManager(process.argv[2]).catch(err => console.error(err));
