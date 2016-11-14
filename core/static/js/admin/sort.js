(function () {
  // Use jQuery from Django admin.
  var jQuery = django.jQuery;

  jQuery(document).ready(function () {
    // Set CSRF token for AJAX requests.
    function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
          var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }

    function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    var csrftoken = getCookie('csrftoken');
    jQuery.ajaxSetup({
      beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      }
    });

    // Add data-id to sortable items from action's select boxes.
    var $resultList = jQuery('#result_list');
    var $resultRows = $resultList.find('> tbody > tr');
    $resultRows.each(function (index) {
      var modelId = jQuery(this).find('> .action-checkbox > .action-select').val(),
        modelPosition = jQuery(this).find('> .field-position').html();

      jQuery(this).attr('data-id',
        '{"id":' + modelId + ', "position":' + modelPosition + '}');
    });

    // Make results table sortable.
    var $resultBody = $resultList.find('> tbody');
    if ($resultBody.length > 0) {
      var sort = Sortable.create($resultBody.get(0), {
        animation: 150,
        handle: '.field-drag_handle',
        onUpdate: function (event) {
          jQuery.ajax({
            url: 'reorder/',
            data: JSON.stringify(sort.toArray()),
            type: 'PUT',
            success: function(data) {
              console.log(data);
            }
          });
        }
      });
    }
  });
})();
