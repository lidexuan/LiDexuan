 var now = Date.now();
 var appId = 'A6918573369588',
     appKey = SHA1("A6918573369588" +"UZ" +"20C93719-0DE5-8C9B-2F05-36D9BB835C02" +"UZ" + now) +"." + now;


 function fnGet(path, filter, callback) {
     api.showProgress({
         title: '加载中',
         modal: true
     });

     api.ajax({
         url: 'https://d.apicloud.com/mcm/api/' + path + '?filter=' + JSON.stringify(filter),
         method: 'get',
         timeout: 5,
         dataType: 'json',
         headers: {
            "X-APICloud-AppId": appId,
            "X-APICloud-AppKey": appKey
         }
     }, function(ret, err) {
         api.hideProgress();
         callback(ret, err);
     });
 };

 function fnPost(path, data, contentType, callback, isLogin, isPut) {
     var headers = {
        "X-APICloud-AppId": appId,
        "X-APICloud-AppKey": appKey
     };

     if (contentType) {
         headers["Content-Type"] = contentType
     }

     if (isLogin) {
         if (!$api.getStorage('loginInfo')) {
             api.openWin({
                 name: 'login_choose',
                 url: './login_choose.html'
             });
             return;
         }
         var accessToken = $api.getStorage('loginInfo').id;

         headers["authorization"] = accessToken;
     }

     api.showProgress({
         title: '加载中',
         modal: true
     });

     api.ajax({
         url: 'https://d.apicloud.com/mcm/api/' + path,
         method: isPut ? 'put' : 'post',
         timeout: 5,
         dataType: 'json',
         returnAll: false,
         headers: headers,
         data: data
     }, function(ret, err) {
         api.hideProgress();
         callback(ret, err);
     });
 };
