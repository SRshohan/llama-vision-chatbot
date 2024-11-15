import ollama

def multimodal_response(description, image=None):
    message = {
        'role': 'user',
        'content': f"{description}"
    }

    if image is None:
        response = ollama.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': f"{description}",
        }]
    )
    else:
        if image:
            # for i in image:
            message['images'] = image
        response = ollama.chat(
            model='llama3.2-vision',
            messages=[message]
        )
    response = response['message']['content']
    return response



