(function () {
  // Use jQuery from Django admin.
  var jQuery = django.jQuery;

  jQuery(document).ready(function () {
    // Make results table sortable.
    var $resultBody = jQuery('#result_list').find('> tbody');
    if ($resultBody.length > 0) {
      var sort = Sortable.create($resultBody.get(0), {
        animation: 150,
        handle: ".field-drag_handle"
      });
    }
  });
})();
