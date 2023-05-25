import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const fs = require('fs');
const fileContents = fs.readFileSync('../config.origin.yml', 'utf8');
const data = yaml.safeLoad(fileContents);
var gitalk = new Gitalk({
    clientID: data['id'],
    clientSecret: data['clientSecret'],
    repo: data['repo'],
    owner: data['owner'],
    admin:  ['admin'],
    id: location.pathname,      // Ensure uniqueness and len
    distractionFreeMode: false  // Facebook-like distraction
})
gitalk.render('gitalk-container')
