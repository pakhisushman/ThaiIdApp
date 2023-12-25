from flask import Flask, request, jsonify
import cv2
import easyocr
from PIL import Image
import numpy

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        # Read image and perform OCR
        img = cv2.imdecode(numpy.fromstring(request.files['image'].read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('grayimg.jpg', gray_img)
        reader = easyocr.Reader(['en'])
        result = reader.readtext('grayimg.jpg')
        new_result = [resultInternal[1] for resultInternal in result]

        # Extract relevant information (customize based on your OCR output)
        identification_number = new_result[4]
        name = new_result[10]
        last_name = new_result[12]
        date_of_birth = new_result[14]

        # Store the extracted information in the database (you need to implement this)
        # For now, let's just return the data in JSON format
        data_to_store = {
            'identification_number': identification_number,
            'name': name,
            'last_name': last_name,
            'date_of_birth': date_of_birth
        }

        # You can store the data in the database here
        # For demonstration, we'll just return the data as JSON
        return jsonify(data_to_store)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)










# # This is a sample Python script.

# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import easyocr
# import cv2
# import openai
# from flask import Flask, request, jsonify

# app = Flask(__name__)


# # def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# image_path = 'thai_id_card.jpg_large'
# img = cv2.imread(image_path)
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imwrite('grayimg.jpg', gray_img)
# reader = easyocr.Reader(['en'])
# result = reader.readtext('grayimg.jpg')
# # print(result)
# new_result = [resultInternal[1] for resultInternal in result]
# print(new_result)
# # print(result[0][1])
# # Press the green button in the gutter to run the script.
# # Set your OpenAI GPT-3 API key
# # openai.api_key = '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'
# #
# # # Define a conversation as a list of messages
# # # conversation = [
# # #     {"role": "system", "content": "You are a helpful assistant."},
# # #     {"role": "user", "content": "Who won the world series in 2020?"},
# # # ]
# #
# # # Example user queries
# # # user_queries = [
# # #     "Who won the MVP?",
# # #     "How many games did they win?",
# # #     "Where was it played?"
# # # ]
# #
# # # Extend the conversation with user queries
# # # for query in user_queries:
# # #     conversation.append({"role": "user", "content": query})
# #
# # # Send the conversation to GPT-3 for a continuation
# # response = openai.Completion.create(
# #     model="text-davinci-003",  # or another available model
# #     prompt = "Say this is a test",
# #     max_tokens=7,
# #     temperature=0,
# #     # messages=conversation
# # )
# #
# # # Extract and print the assistant's reply
# # # assistant_reply = response['choices'][0]['message']['content']
# # print(response)
# # # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# # # 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



