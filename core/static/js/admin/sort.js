(function () {
  // Use jQuery from Django admin.
  var jQuery = django.jQuery;

  jQuery(document).ready(function () {
    var $resultList = jQuery('#result_list');

    // Add data-id to sortable items from action's select boxes.
    var $resultRows = $resultList.find('> tbody > tr');
    $resultRows.each(function (index) {
      var modelId = jQuery(this).find('> .action-checkbox > .action-select').val(),
        modelPosition = jQuery(this).find('> .field-position').html();

      jQuery(this).attr('data-id',
        '{id:' + modelId + ', position:' + modelPosition + '}');
    });

    // Make results table sortable.
    var $resultBody = $resultList.find('> tbody');
    if ($resultBody.length > 0) {
      var sort = Sortable.create($resultBody.get(0), {
        animation: 150,
        handle: '.field-drag_handle',
        onUpdate: function (event) {
          console.log(sort.toArray());
        }
      });
    }
  });
})();
