var molhokwai={
	util : {
		object : {
			/*
				obj:
					the object
				kfl: list
					-	function for key
					-	optional params dict
				vfl: list
					-	function for value
					-	optional params dict
			*/
			walk : function(obj, kfl, vfl){
				for(k in obj){
                    var p = null;
					if (kfl){
						p = kfl.length>1 ? kfl[1] : null;
						kfl[0](k, p);
					}
					if (vfl){
						p = vfl.length>1 ? vfl[1] : null;
						vfl[0](obj[k], p);
					}
				}
			}
		}
	}
};

