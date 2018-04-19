var update_running=false;



function GetUpdates(refresh_button) {
    console.log('in Refresh()')
    var scroll_down = document.getElementById("auto-scroll").checked;
    var auto_update = document.getElementById("auto-update").checked;
    var e = document.getElementById("ddlViewBy");
    var refresh_delay = parseInt(document.getElementById("input-delay").value);

    $('.ajaxProgress').show();
    $.ajax({
        type: "GET",
        url: "/updates/getupdates/",
        dataType: "json",
        async: true,
        data: {
            csrfmiddelwaretoken: '{{ csrf_token }}'
        },
        success: function(json) {
            var table=json.table

            $('#table_updates > tbody:last-child').append(table);
            if(json.hasOwnProperty('result')){
                console.log("FOUND RESULT!")
                var res_html="<a href=".concat(json.result).concat(">RESULT-FILE</a>")
                console.log(res_html)
                $('#table_updates > tbody:last-child').append(res_html);
            }
            $('.ajaxProgress').hide();
            if (scroll_down) {
                var objDiv = document.getElementById("console");
                objDiv.scrollTop = objDiv.scrollHeight;
            }
            if ((!refresh_button && auto_update) || (refresh_button && auto_update && !update_running)) {
                console.log("in TimeOut")
                setTimeout(function(){GetUpdates();}, refresh_delay);
                update_running=true;
            }
            if (!auto_update) {
                console.log("set running false")
                update_running=false;

            }

        }
    });
};


$(function () {
    $('.button-checkbox').each(function () {

        // Settings
        var $widget = $(this),
            $button = $widget.find('button'),
            $checkbox = $widget.find('input:checkbox'),
            color = $button.data('color'),
            settings = {
                on: {
                    icon: 'glyphicon glyphicon-check'
                },
                off: {
                    icon: 'glyphicon glyphicon-unchecked'
                }
            };

        // Event Handlers
        $button.on('click', function () {
            $checkbox.prop('checked', !$checkbox.is(':checked'));
            $checkbox.triggerHandler('change');
            updateDisplay();
        });
        $checkbox.on('change', function () {
            updateDisplay();
        });

        // Actions
        function updateDisplay() {
            var isChecked = $checkbox.is(':checked');


            // Set the button's state
            $button.data('state', (isChecked) ? "on" : "off");

            // Set the button's icon
            $button.find('.state-icon')
                .removeClass()
                .addClass('state-icon ' + settings[$button.data('state')].icon);

            // Update the button's color
            if (isChecked) {
                $button
                    .removeClass('btn-default')
                    .addClass('btn-' + color + ' active');
            }
            else {
                $button
                    .removeClass('btn-' + color + ' active')
                    .addClass('btn-default');
            }
        }

        // Initialization
        function init() {

            updateDisplay();

            // Inject the icon if applicable
            if ($button.find('.state-icon').length == 0) {
                $button.prepend('<i class="state-icon ' + settings[$button.data('state')].icon + '"></i> ');
            }
        }
        init();
    });
});

console.log('LoadUpdates')
GetUpdates(false)


