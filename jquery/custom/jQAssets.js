try {
    if(assets){
        /* check passed */
    }
    else{
        assets = {};
        assets['tag'] = {'img': [], 'a' : [], 'embed' : [], 'object' : []};
    }
}
catch(e){
   var assets = {};
    assets['tag'] = {'img': [], 'a' : [], 'embed' : [], 'object' : []};
}

/* 'quick' method, not guaranteed (html incorrectly formatted...) */
assets['getFromParsedHtml'] = function(params){
	/* . Get the body html:
  		-	Append it to given element
  		-	Get given element assets (images, embeds, links...)
	*/
	var arbC = assets.remote.bodyContainer;
	arbC.element = document.createElement('iframe');
	arbC.element.id = arbC.id;

	try{ $(arbC.element).html(params.html); }
	catch(e){ console.log(e.description); }

	for(tag in assets.tag){
		assets.tag[tag] = $(arbC.element).find(tag);
	}
	
};
assets['get'] = function(params){
    if(!params.url || !params.callback){
        throw "params.url && params.callback required in assets.get function"
    }
    $.ajax({
        url : assets.remote.relayUrl.replace('%(url)s', params.url),
        type : 'GET',
        success : function(body){
			/* disable unused widget script for no redirection */
			body = body.replace('widget.js', '__widget__');
			/* get */
	        assets.getFromParsedHtml({ html:body });
            params.callback({ assets:assets });
        }
    })
};
assets['remote'] = {
    /* default, overwriteable url */
    relayUrl : 'http://molhokwai-net.appspot.com/a/relay?url=%(url)s&output=html',
	bodyContainer : {
		element : null,
    	/* default, overwriteable id */
		id : 'remoteBodyContainer'
	}
};
