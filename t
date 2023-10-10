{% if user.is_authenticated %}
    {% if user.is_staff %}
        <p>You have staff access.</p>
    {% else %}
        <p>You have regular user access.</p>
    {% endif %}
{% else %}
    <p>You are not logged in.</p>
{% endif %}



center_cell = worksheet.cell(
            row=worksheet.max_row // 3,
            column=worksheet.max_column // 2
        )


# Load the new image
new_image_path = obj.image_field.path
new_img = Image(new_image_path)