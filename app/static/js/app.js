var stampApp = angular.module('stampApp', ['ngRoute']);

stampApp.config(function($interpolateProvider, $routeProvider) {
		// Change Angular delimiter notation so it does not conflict with Jinja2
        $interpolateProvider.startSymbol('{a').endSymbol('a}');

        $routeProvider
		.when('/',
		{
			controller: 'stampCtrl',
			templateUrl: '../static/partials/stamp_list.html'
		})
		.otherwise({ redirectTo: '/' });
});

stampApp.controller('stampCtrl', function($scope, $http) {
	$http.get('/stamp/api/v1.0/stamps').success(function(data){
		$scope.stamps = data;
	}).error(function(data){
		console.log('Error getting data in stampCtrl');
	})
})