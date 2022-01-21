$RequestHeader = @{};
$RequestHeader.Add("Authorization", "token c0efa4be06a92f8b60dc4f818b30eb468041fdd7");
$api_host = "http://localhost:8000"
#$final_url = "{0}{1}" -f $api_host,'/api/cart-items/'
#Invoke-RestMethod http://localhost:8000/api/cart-items/ -Method GET -Header(@{"Authorization" = "token c0efa4be06a92f8b60dc4f818b30eb468041fdd7"})

#################################################################################################################################
#GET Method for Fetch All objects
$GetAllUrl = "$api_host/api/cart-items/"
#Invoke-RestMethod $GetAllUrl -Method GET -Headers $RequestHeader
#################################################################################################################################

#################################################################################################################################
#POST Method for Cretae Resource in database
$PostUrl = "$api_host/api/cart-items/"
$PostBody = @{
    product_name="Son Mobile";
    product_price=2000.0;
    product_quantity=20
}
#Invoke-RestMethod $PostUrl -Method POST -Headers $RequestHeader -Body($PostBody | ConvertTo-Json) -ContentType "application/json"
#########################################################################################

#################################################################################################################################
#GET Method for Fetch Single object
$GetSingleUrl = "$api_host/api/cart-items/3"
#Invoke-RestMethod $GetSingleUrl -Method GET -Headers $RequestHeader
#################################################################################################################################


#################################################################################################################################
#PUT Method for Update Single object
$PutUrl = "$api_host/api/cart-items/3"
$PutBody = @{
    product_name="MI Mobile";
    product_price=2000.0;
    product_quantity=20
}
#Invoke-RestMethod $PutUrl -Method PUT -Headers $RequestHeader -Body($PutBody | ConvertTo-Json) -ContentType "application/json"
#################################################################################################################################


#################################################################################################################################
#DELETE Method for Delete Single object
$DeleteUrl = "$api_host/api/cart-items/3"
Invoke-RestMethod $DeleteUrl -Method DELETE -Headers $RequestHeader
#################################################################################################################################