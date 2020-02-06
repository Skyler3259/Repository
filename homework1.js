// Feel free to mess with this function, it just lets the button do something.
function payNow(total) {
    alert("Pay Dave's Shop $" + (total + (total * .25)));
}
/*
    === Exercise 1 (1pt) === 
    Create a greeting variable that you will use to greet yourself. (0.5)
    Write this greeting out to the 'greeting' element on Homework1.html (0.5)
    ** Hint ** It may be useful to use the getElementById().textContent to set the message
    The greeting at a MINIMUM must have your Name.
    Ex: Hello Dave Debreceni, please verify your order:
*/

var greeting = "Hello Skyler"
    document.getElementById('greeting').textContent = greeting;


/*
    === Exercise 2 (3pt) ===
    Create your shopping cart. You will need to create table rows and table cells in Homework1.html.
    Your shopping cart should have a minimum of 3 items.  Below you will create a variable
    for each item and assign it it's price. Then update the elementId with that price.
    For example, you may have something like this:
    <tr>
      <td>Almond Milk</td>
      <td id="almondMilk"></td>
    </tr>
    var almondMilk = 2.97;
    document.getElementById('almondMilk').textContent = '$' + almondMilk;
*/
    var pizza = 1.95;
    document.getElementById('pizza').textContent = '$' + pizza;

/*
    === Exercise 3 (1pt) ===
    Create a variable called total and add all your items up and assign that number to it.
    Set the elementId 'total' with this value.
*/