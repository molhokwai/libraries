/* SCRIPT NOT OPERATIONAL 
	-	For Incorrect/Invalid html, cases to be implemented in RegExp...
*/

try {
    if(assets){
        /* check passed */
    }
    else{
        assets = {};
        assets['tagList'] = {'img': [], 'a' : [], 'embed' : [], 'object' : []};
    }
}
catch(e){
   var assets = {};
    assets['tagList'] = {'img': [], 'a' : [], 'embed' : [], 'object' : []};
}

assets['getFromHtmlString'] = function(html){
	/* . Get the body html:
		-	Regex to find assets 
		.	Append 
	*/
	while(html.indexOf("\r")>=0 || html.indexOf("\n")>=0){
		html = html.replace("\r", "").replace("\n", "");
	}

	for(tag in assets.tagList){
		var results = new RegExp('<'+tag+'(.*)\\/{0,1}>$').exec(html);
		for(i in results){
			assets.tagList[tag].push($.parseXML(results[i][1]));
		}
	}
};
assets['getAssetAttribute'] = function(attr){
	/*	Regexp to get the given attribute from asset string
		Or direct $(...).attr(attr)
	*/
};
assets['get'] = function(url){
	$.ajax({
		url : assets.remote.relayUrl.replace('%(url)s', url), 
		type : 'GET',
		success : function(body){
			assets.getFromHtmlString(body);
		}
	})
};
assets['remote'] = {
    /* default, overwriteable url */
    relayUrl : 'http://molhokwai-net.appspot.com/a/relay?url=%(url)s&output=html'
};

/* pseudo code * /
$.ajax({
	type : 'BODY',
	success : function(body){
 	/ * . Get the two calendar images:
	  	Sample sources:
	  	- images/11.jpg (12.jpg, 13.jpg..., (0 - 13).jpg)
	  	- images/crocodile.jpg right next to previous image...
		. Display
 	* /
}
});
*/
