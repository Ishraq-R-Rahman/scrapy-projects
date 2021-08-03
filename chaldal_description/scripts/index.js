const dotenv = require('dotenv')

dotenv.config( { path : '../config/config.env'} )


const url = process.env.START_URLS.split(',')
// process.env.START_URLS = url
// link = process.env.START_URLS
console.log(url);

const exec = require('child_process').exec
const path = require('path')
// const {spawn} = require('child_process')

// const childProcess = spawn('scrapy', [
//     'crawl', 'dove',
//     '-o','product.json'
// ])

// childProcess.stderr.on('data' , data => console.log(data))

//SCRAPING THE WEBSITE

const file_path = path.join(__dirname, '../crawlers/crawler.py')

exec( 'python ' + file_path, function(err,stdout,stderr){
    if( err ){
        console.log(stderr);
        return;
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
} )