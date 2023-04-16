import streamlit as st
import os 
from PIL import Image
from pillow_heif import register_heif_opener

class heic_to_img_converter():
    
    def __init__(self) -> None:
        register_heif_opener()
        
        self.uploaded_files = ""
        
        self.bytes_data = ""
        
        self.upload_file()
        

            
    def upload_file(self):
        
        self.uploaded_files = st.file_uploader("Choose a file.", accept_multiple_files= True)
            
        if self.uploaded_files:
            
            if not os.path.exists('converted_images'):
                os.makedirs('converted_images')
            
            st.write("You have selected files:")
            for uploaded_file in self.uploaded_files:
                self.bytes_data = uploaded_file.read()    
                st.write("filename:", uploaded_file.name)
            
            if st.button("Convert Images HEIC to JPG"):
                self.convert_file()
            
        else:
            st.write("Please select a file.")
            
       
            
                
            
    def convert_file(self):
            
        for uploaded_file in self.uploaded_files:
            self.file_name = uploaded_file.name.lower()
            

            if self.file_name.endswith('.heic'):
                

                with Image.open(uploaded_file) as heif_file:
                    
                    self.new_file_name = os.path.basename(self.file_name).replace('.heic','.jpg')
                    
                    self.new_file_path = os.path.abspath(os.path.join('converted_images', self.new_file_name))
                    heif_file.save(self.new_file_path, format='JPEG')
        
        st.write("All job is done!")
        
                    
abc = heic_to_img_converter()
           
            
        
        


