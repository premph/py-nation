<?php
<form action='/upload.html/' method='post'>{% csrf_token %}
{{ form.as_p }}
<input type='submit' value='Submit' />
</form>

?>