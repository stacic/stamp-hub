var stampApp = angular.module('stampApp', []);

stampApp.config(function($interpolateProvider){
	// Change Angular delimiter notation so it does not conflict with Jinja2
    $interpolateProvider.startSymbol('{a').endSymbol('a}');
});

stampApp.controller('stampCtrl', function($scope, $http) {
	$http.get('/stamp/api/v1.0/stamps').success(function(data){
		$scope.stamps = data;
	})
})