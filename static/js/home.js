function state_politicians_detail() {
//     console.log(typeof(data_set));
//     var toSend = JSON.stringify(data_set);
//     // console.log(toSend);
//     $.ajax({
//         url: '{% url "politiciandetails" %}',
//         type: 'POST',
//         data: {
//             'pk':data_set,
//             'csrfmiddlewaretoken': '{{ csrf_token }}',
//         },
//         success: function (data){
//                     console.log(data);
//                  }
//     });
// }
    window.location.href = 'politician_details';
}
// $(document).ready(function(event){
//     $(document).on('click', '#like', function(event){
//         event.preventDefault();
//         var pk = $(this).attr('value');
//         $.ajax({
//             type: 'POST',
//             url: '{% url "politiciandetails" %}',
//             data: {
//                 'pk':pk,
//             'csrfmiddlewaretoken': '{{ csrf_token }}',
//         },
//             datatype: 'json',
//         });
//     });
//   });