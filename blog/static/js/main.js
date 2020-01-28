$(document).ready(
    function(){
            $(".toggle").on("click", function(){
                if($(".item").hasClass("active")){
                    $(".nav-bar").children().removeClass("active");
                    console.log("hello")
                }
                else{
                    $(".item").addClass("active");
                }
            });
        }
);