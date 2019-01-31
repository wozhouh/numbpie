$(document).ready(function () {
    // Init
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();

    // Upload Preview
    function readImageURL(input, eltId) {
      if (input.files && input.files[0]) {
          var reader = new FileReader();
          reader.onload = function (e) {
              $('#' + eltId).css('background-image', 'url(' + e.target.result + ')');
              $('#' + eltId).hide();
              $('#' + eltId).fadeIn(650);
          }
          reader.readAsDataURL(input.files[0]);
      }
    }
    // $('#show-popimg').click(function () {
    //     $('#scroll_tree').show();
    //     $('#popimg_predict_btn').show();
    //     $('#upload_sec').hide();
    // });
    //
    // $('#show-upload').click(function () {
    //     $('#upload_sec').show();
    //     $('#scroll_tree').hide();
    // });

    $('.select2').select2();
    $('#gan_check').click(function() {
        $("#dropdown").toggle(this.checked);
    });

    // console.log($("div[data-p='144.50'][style != 'top: 0px; left: 0px; width: 450px; height: 580px; position: absolute; overflow: hidden; perspective: 144.5px;']").find("img").attr("src"))

    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').hide();
        readImageURL(this, 'imagePreview');
    });

    // Predict
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);
        if (document.getElementById('gan_check').checked) {
          $.ajax({
              type: "POST",
              url: "/writetxt",
              dataType: "text",
              data: {"file": "checked", "value": true},
              async: false
            }).done(function () {
          });
          var select_1 = document.getElementById("select_feature");
          var select_2 = document.getElementById("select_texture");
          var select_3 = document.getElementById("select_action");
          for (var i = 0; i < select_1.options.length; i++) {
            if (select_1.options[i].selected) {
              $.ajax({
                  type: "POST",
                  url: "/writetxt",
                  dataType: "text",
                  data: {"file": "feature", "value": select_1.options[i].value},
                  async: false
                }).done(function () {
              });
            }
          }
          for (var i = 0; i < select_2.options.length; i++) {
            if (select_2.options[i].selected) {
              $.ajax({
                  type: "POST",
                  url: "/writetxt",
                  dataType: "text",
                  data: {"file": "texture", "value": select_2.options[i].value},
                  async: false
                }).done(function () {
              });
            }
          }
          for (var i = 0; i < select_3.options.length; i++) {
            if (select_3.options[i].selected) {
              $.ajax({
                  type: "POST",
                  url: "/writetxt",
                  dataType: "text",
                  data: {"file": "action", "value": select_3.options[i].value},
                  async: false
                }).done(function () {
              });
            }
          }
        } else {
          $.ajax({
              type: "POST",
              url: "/writetxt",
              dataType: "text",
              data: {"file": "checked", "value": false},
              async: false
            }).done(function () {
          });
        }

        // Show loading animation
        $(this).hide();
        $('.loader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function (data) {
                // Get and display the result
                $('.loader').hide();
                if (document.getElementById('gan_check').checked) {
                  $('#gan_info_sec').show();
                  $('#gan_info_label').show();
                } else {
                  $('#gan_info_sec').hide();
                  $('#gan_info_label').hide();
                }

                // Force refresh
                $("#rec1_img").attr('src', "../static/rec_images/rec1.jpg"+"?t=" + Math.random());
                $("#rec2_img").attr('src', "../static/rec_images/rec2.jpg"+"?t=" + Math.random());
                $("#rec3_img").attr('src', "../static/rec_images/rec3.jpg"+"?t=" + Math.random());
                $("#rec4_img").attr('src', "../static/rec_images/rec4.jpg"+"?t=" + Math.random());
                $("#rec5_img").attr('src', "../static/rec_images/rec5.jpg"+"?t=" + Math.random());

                $.ajax({
                    type: "GET",
                    url: "static/rec_accuracy/1.txt",
                    dataType: "text",
                    async: false
                  }).done(function (acc) {
                    $("#accuracy1").html(acc);
                });
                $.ajax({
                    type: "GET",
                    url: "static/rec_accuracy/2.txt",
                    dataType: "text",
                    async: false
                  }).done(function (acc) {
                    $("#accuracy2").html(acc);
                });
                $.ajax({
                    type: "GET",
                    url: "static/rec_accuracy/3.txt",
                    dataType: "text",
                    async: false
                  }).done(function (acc) {
                    $("#accuracy3").html(acc);
                });
                $.ajax({
                    type: "GET",
                    url: "static/rec_accuracy/4.txt",
                    dataType: "text",
                    async: false
                  }).done(function (acc) {
                    $("#accuracy4").html(acc);
                });
                $.ajax({
                    type: "GET",
                    url: "static/rec_accuracy/5.txt",
                    dataType: "text",
                    async: false
                  }).done(function (acc) {
                    $("#accuracy5").html(acc);
                });
                $('#result').fadeIn(600);
            },
        });
    });

});
