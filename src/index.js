const fetch = require('node-fetch')
const parseString = require('xml2js').parseString
const util = require('util')
const fs = require('fs-extra')
const { fileURLToPath } = require('url')

const parseXml = util.promisify(parseString)

async function getEpisodes() {
    const response = await fetch('https://feeds.fireside.fm/thecodekitchen/rss')
        .then(_ => _.text())
        .then(_ => parseXml(_))

    return response.rss.channel[0].item;
}


async function main() {

    const episodes = await getEpisodes();
    const content = episodes.map(ep => {
        return `<h2>${ep.title}</h2>${ep['content:encoded']}
            <iframe src="${ep['fireside:playerURL']}?base_slug=thecodekitchen&theme=dark" width="740" height="200" frameborder="0" scrolling="no"></iframe>
        `.trim()
    }).join('')

    const template = await fs.readFile('./template.html', 'utf8')
    console.log(template);

    const indexHtml = template.replace('{{CONTENT}}', content);

    await fs.writeFile('./docs/index.html', indexHtml);

}




main()