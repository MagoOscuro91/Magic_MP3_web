<div id="donate-button-container">
    <div id="donate-button"></div>
    <script src="https://www.paypalobjects.com/donate/sdk/donate-sdk.js" charset="UTF-8"></script>
    <script>
    PayPal.Donation.Button({
    env:'production',
    hosted_button_id:'JEJEVBNDSU594',
    image: {
    src:'https://www.paypalobjects.com/es_ES/ES/i/btn/btn_donateCC_LG.gif',
    alt:'Botón Donar con PayPal',
    title:'PayPal - The safer, easier way to pay online!',
    }
    }).render('#donate-button');
    </script>
    </div>
    