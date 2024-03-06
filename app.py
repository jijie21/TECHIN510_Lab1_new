import streamlit as st

def create_section(header, markdown_content, divider_option='blue'):
    st.header(f'{header}', divider=divider_option)
    st.markdown(markdown_content)

# Create two columns for the introduction
col1, col2 = st.columns(2)

with col1:
    st.image('./IMG_0969.JPG', caption=None, width=250, channels='RGB', output_format='JPG')

with col2:
    st.title('Hi, I am Jackie :sunglasses:')
    st.header('I am a product designer based in Bellevue, WA')

education_content = '''**BFA in Interaction Design** @ California College of the Arts  
**MS in Technology Innovation** @ University of Washington'''
create_section('Education :mortar_board:', education_content)

work_experience_content = '''**Product Design Intern** @ DocuSign in San Francisco  
**Digital Interaction Designer** @ TANG UX in Shanghai'''
create_section('Work Experience :female-technologist:', work_experience_content)

hobbies_interests_content = '''Fabricator :hammer_and_wrench:  
Cafe Enthusiast :coffee:  
Music Lover :notes:  
Beginner Baker :cake: & Bartender :cocktail:'''
create_section('Hobbies & Interests :smiling_face_with_3_hearts:', hobbies_interests_content)

# Contact information
contact_info = '''**Email :** jijie21@uw.edu  
**Phone :** +1 425 495 73944  
**Instagram :** jackieji21  
**Website :** jackieji.me'''
create_section('Contact me :e-mail: ', contact_info)


my_work = '''Check out my work below:'''
create_section('My work :pizza: ', my_work)
st.image('daysphere.png', caption=None, width=180, channels='RGB', output_format='PNG')
st.link_button("View project →", "https://jackieji21.notion.site/Project-Archive-a63ad34de2ba49f39d13d677d9349c5d?pvs=4")