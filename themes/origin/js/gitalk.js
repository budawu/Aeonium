fetch('../../themes/origin/config.origin.yml')
    .then((response) => response.json())
    .then((json) => console.log(json));
var gitalk = new Gitalk({
    clientID: 'id',
    clientSecret: 'clientSecret',
    repo: 'repo',
    owner: 'owner',
    admin: 'admin',
    id: location.pathname,      // Ensure uniqueness and len
    distractionFreeMode: false  // Facebook-like distraction
})
gitalk.render('gitalk-container')
