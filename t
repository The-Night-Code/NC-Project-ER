{% if user.is_authenticated %}
    {% if user.is_staff %}
        <p>You have staff access.</p>
    {% else %}
        <p>You have regular user access.</p>
    {% endif %}
{% else %}
    <p>You are not logged in.</p>
{% endif %}
