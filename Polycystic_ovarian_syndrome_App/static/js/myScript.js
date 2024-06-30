function validateUser(){
                var name=document.getElementById('uname').value;
                var contactNo=document.getElementById('contactNo').value;
                var emailId=document.getElementById('emailId').value;
                var address=document.getElementById('address').value;
                var username=document.getElementById('username').value;
                var password=document.getElementById('password').value;
              
                if(name==""){
                    window.alert('Please provide Name');
                    return false;
                }
                else if(contactNo==""){
                    window.alert('Please provide Contact Number');
                    return false;
                }
                else if(contactNo.length!=10){
                    window.alert('Please provide valid Contact Number');
                    return false;
                }
                else if(emailId==""){
                    window.alert('Please provide EmailID');
                    return false;
                }
                else if(!/(.+)@(.+){2,}\.(.+){2,}/.test(emailId)){
                    window.alert('Please provide Valid EmailID');
                    return false;
                }
                else if(address==""){
                    window.alert('Please provide Address');
                    return false;
                }
                else if(username==""){
                    window.alert('Please provide Username');
                    return false;
                }
                else if(password==""){
                    window.alert('Please provide Password');
                    return false;
                }
                
                return true;
            }

            function validateLogin(){
                var username=document.getElementById('username').value;
                var password=document.getElementById('password').value;

                if(username==""){
                    window.alert('Please provide Username');
                    return false;
                }
                else if(password==""){
                    window.alert('Please provide Password');
                    return false;
                }
                return true;
            }


            function validateForm(){
                var height=document.getElementById('height').value;
                var weight=document.getElementById('weight').value;
                var bmi=document.getElementById('bmi').value;
                var hirsutism=document.getElementById('hirsutism').value;
                var skin=document.getElementById('skin').value;
                var acene=document.getElementById('acene').value;
                var menstrual=document.getElementById('menstrual').value;
                var sleep=document.getElementById('sleep').value;
                var hair=document.getElementById('hair').value;
              
                if(height==""){
                    window.alert('Please provide height');
                    return false;
                }
                else if(parseFloat(height) >= 250.00){
                    window.alert('Height should be less than 250cm');
                    return false;
                }
                else if(weight==""){
                    window.alert('Please provide weight');
                    return false;
                }
                else if(parseFloat(weight) >= 120.00){
                    window.alert('Weight should be less than 120kg');
                    return false;
                }
                else if(bmi==""){
                    window.alert('Please provide BMI');
                    return false;
                }
                else if(parseFloat(bmi) >= 40.00){
                    window.alert('BMI should be less than 40');
                    return false;
                }
                else if(hirsutism=="-1"){
                    window.alert('Please provide hirsutism');
                    return false;
                }
                else if(skin=="-1"){
                    window.alert('Please provide skin');
                    return false;
                }
                else if(acene=="-1"){
                    window.alert('Please provide acene');
                    return false;
                }
                else if(menstrual=="-1"){
                    window.alert('Please provide menstrual count');
                    return false;
                }
                else if(sleep=="-1"){
                    window.alert('Please provide sleep');
                    return false;
                }
                else if(hair=="-1"){
                    window.alert('Please provide hair');
                    return false;
                }
                return true;
            }
