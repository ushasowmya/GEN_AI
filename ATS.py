from utilities import get_embedding, extract_text_from_pdf, compute_similiarity
import streamlit as st
import io

#jd = "We are looking for AWS, python developer who has 5 years of experience"

uploaded_resume_file = st.file_uploader("upload your file")
if uploaded_resume_file is not None:
   pdf_bytes = uploaded_resume_file.getvalue()
   st.write(uploaded_resume_file.name)
   jd = st.text_area("Enter the Job Description")
   st.button("Submit")

   resume_text = extract_text_from_pdf(io.BytesIO(pdf_bytes))
   compute_similiarity(resume_text,jd)
   if compute_similiarity(resume_text, jd) > 0.5:
     print("Matched")
     st.warning("Matched")
   else:
     print("Not Matched")
     st.warning('Job Description and Resume is not matched')

else:
 st.write("please upload a file")


  
  #Read the file contents as bytes
 # file_contents = uploaded_resume_file.read()
  
  
  # Decode the bytes to a string (if needed)
  #try:
   #   decoded_contents = file_contents.decode('utf-8', errors='ignore')
  #except UnicodeDecodeError:
   #     decoded_contents = "File contains non-UTF-8 characters"
  
  #st.write(decoded_contents)





#if uploaded_resume_file is not None:
#file_content = uploaded_resume_file.getvalue().decode('utf-8')
#print(file_content)
#Save the file contents to the text file
#   with open('uploaded_resume_file.txt') as f:
#     f.write(file_content)
#   st.success("File saved successfully!")



#resume_file  = st.write(uploaded_resume_file) ###Check the file format





#resume_embedding = get_embedding(resume_text)

#resume_text = extract_text_from_pdf("/Users/ushasowmyavasamsetti/Downloads/Resume_usha_2024.pdf")








