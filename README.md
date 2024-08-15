# Avani
An automated tool to segment, transcribe, translate, and process audio responses to a set of predetermined questions by farmers in Marathi to help understand their problems

## Steps to run

1. Clone the repo
   
2. Add the following details to the backend
   
   * In utilities/db_utils.py, add your SQL database details. For instance:
     
   ```
   connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db="", # add DB name
        host="", # add host name
        password="", # add password
        read_timeout=timeout,
        port=27329,
        user="", # add username
        write_timeout=timeout,
    )
   ```
   * In controllers/audio_controller.py, complete the process_audio function to link to your AI model for processing.
   ```
   process_audio(audio) # Link to your AI Model functions
   ```

3. Host the backend on any server and generate a URL

4. Replace the backend URL in the script.js file in the frontend folder, for instance
   ```
   fetch('BACKEND_URL/process_audio', { // Replace with your actual API URL
            method: 'POST',
            body: formData,
   })
   ```
5. The website is ready to be hosted and used
