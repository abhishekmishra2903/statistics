#!/usr/bin/env python
# coding: utf-8

# In[32]:
import streamlit as st

with st.sidebar:
    unit=st.selectbox(label="Select the Unit",options=["1. Introduction to Statistics",
                                                      "2. Descriptive Statistical Analytics",
                                                      "3. Probability Theory & Distributions",
                                                      "4. Sampling and Confidence intervals",
                                                      "5. Hypothesis testing"])
    st.divider()
    if unit=="1. Introduction to Statistics":
        unit1=st.radio("Select the topic",
        ["Applications of Statistics",
         "Presenting Different Types of Data",
         "Primary Data and Secondary Data",
         "The Numeric Data and Categorical Data",
         "Continuous Frequency Distribution",
         "Statistical Analysis with M.S. Excel"]
         )
        unit2=0
        unit3=0
        unit4=0
        unit5=0


    elif unit=="2. Descriptive Statistical Analytics":
        unit2=st.radio("Select the topic",
        ["Central Tendency – Mean, Median and Mode",
         "Variance and Standard Deviation",
         "The Coefficient of Variation measures",
         "Measure of Skewness",
         "Symmetrical Distribution - Kurtosis",
         "Univariate, Bivariate and Multivariate Analysis"]
         )
        unit1=0
        unit3=0
        unit4=0
        unit5=0

    elif unit=="3. Probability Theory & Distributions":
        unit3=st.radio(
        "Select the topic",
        ["Probability Theory",
         "Fundamental Concepts of Probability",
         "Definitions of Probability",
         "Applying Laws of Probability - Bayes Theorem",
         "Calculating Random Variable",
         "Probability-Distribution with a Case Study"])
        unit2=0
        unit1=0
        unit4=0
        unit5=0
        
    elif unit=="4. Sampling and Confidence intervals":
        unit4=st.radio(
        "Select the topic",
        ["Introduction to Sampling Theory",
         "Sampling Distribution",
         "Using probabilistic Sampling Techniques",
         "Estimating Sampling Errors",
         "Confidence Intervals",
         "Sampling Error and Non-Sampling Error",
         "Central Limit Theorem",
         "Case Study on Sampling Techniques"])
        unit2=0
        unit3=0
        unit1=0
        unit5=0
        
    elif unit=="5. Hypothesis testing":
        unit5=st.radio(
        "Select the topic",
        ["Null Hypothesis and Alternate Hypothesis",
         "Testing Hypothesis for Large Samples",
         "Test for Single Proportion",
         "Test for Difference of Proportions",
         "Testing Hypothesis for Small Samples - T-test",
         "Applications of T-test - P-test",
         "Two-Way Factorial ANOVA",
         "Chi-Square Test and its Application",
         "Testing the Goodness of Fit",
         "Case Study on Hypothesis Testing with Excel"])
        unit2=0
        unit3=0
        unit4=0
        unit1=0
        
    st.divider()
    st.image("C:\\Users\\Miles\\Documents\\Statistics_streamlit\\Abhishek.png",width=160)
    st.subheader('Abhishek Mishra')
    st.text('Author and Developer')
    st.caption(':envelope_with_arrow: patience.might@gmail.com')
    st.link_button(':earth_asia: LinkedIn',"http://www.linkedin.com/in/abhishek-mishra-96b722b3")

if unit1==  'Applications of Statistics':  
    st.markdown('1. Introduction to Statistics')
    st.subheader("1.1 Applications of Statistics")
    st.divider()
    st.write('''Statistics is quite infamous as an intimidating branch of Mathematics
             that offers some cumbersome ways to deal with numerical datasets. 
             A slight change in perspective is needed here. Statistics is a branch of 
             Mathematics that deals with cumbersome numerical datasets on our behalf, to unveil
             hidden patters, express astonishing insights and do some unnerving predictions.''')
    st.markdown('''Wherever, there is a set of numbers involved, statistics has some determining relevance. For example:  
\t :diamonds: Medical statistics – Numbers related to health indicators e.g. glucose, blood-pressure etc.  
\t :diamonds: Environmental statistics – Numbers related to humidity, temperature, pollution etc.  
\t :diamonds: Geo statistics – Numbers like latitude, longitude, Earth’s crust thickness etc.  
\t :diamonds: Social statistics – Social indicators like literacy, demography, sex-ratio etc.  
\t :diamonds: Business analytics – Numbers like revenue, sales, taxation etc.  
……..  
The list can keep going, but this book is going to put more weightage on **Statistics for Business Analytics** for all demonstrations and explanations.  
''')
    with st.expander(":dart: Check your understanding"):
        q1=st.radio('Is Machine Learning a tool of statistics?',['True','False'],horizontal=True,index=None)
        if q1=='True':
            st.markdown(":large_green_circle: _That's right! Machine Learning is a tool that leverages statistics to do predictions_")
        elif q1=='False':
            st.markdown(':large_orange_circle: _Sorry to say, but you should know that Machine Learning is a tool that leverages statistics to do predictions. Statistics is the foundation, and is involved at multiple stages in the back-end of any Machine Learning model._')
    st.markdown(':ballot_box_with_check: **Statistical Approach to Decision-Making**')
    
    st.markdown("""Consider Miss X to be a C.E.O. of a service based I.T. company. For the 
                upcoming month, hiring is scheduled to fill the vacancies for 
                ‘Senior Sales Executive’. She got a proposal to hire candidates who are less 
                than 35 years old. Apparently, a section of the management believes in the 
                hiring of younger talent to be more worthy for the company. Miss X takes a 
                democratic approach and collates the opinions of the management, for both in 
                favour and against. The summary looks like following:
                """)
    col1,col2=st.columns(2)
    with col1:
        st.markdown('**In favour of younger candidates**')
        st.markdown(""":diamonds: Younger employees are more energetic  
:diamonds: More technologically advanced  
:diamonds: More aspiration to grow  
:diamonds: Lesser expectations in terms of compensation  
:diamonds: Family life is less interfering    
""")
    with col2:
        st.markdown('**Against younger candidates**')
        st.markdown(""":diamonds: Younger employees are more into social media  
:diamonds: Struggling to start family  
:diamonds: Emotionally more fragile  
:diamonds: Lesser experience so more inefficient  
:diamonds: Under influence of psychotropic or intoxicating substances
                    """)
                    
    with st.expander(':dart: Give your opinion'):
        q2=st.radio("If you were Miss X, what you would have done?",
                    ["Favour younger candidates","Favour older candidates","Try another approach"],
                    index=None,horizontal=True)
        if q2=="Favour younger candidates" or q2=="Favour older candidates":
            st.markdown(" :laughing: _Are you really able to comprehend anything from the discussed gossip_")
        elif q2=="Try another approach":
            st.markdown(":large_green_circle: _That's correct! This approach is really not providing anything except entertainment_")

    st.markdown("""This approach fails due to following four reasons:  
:diamonds:	It involves more subjectivity and hence more indecisiveness.  
:diamonds:	The points are ambiguous e.g. there isn’t any concrete evidence to establish that who is more into social media and whose emotions are more fragile.  
:diamonds:	It is more oriented to individuals’ character than to their performance and outcome e.g. someone may be more enthusiastic about social media but it doesn’t ascertain that it is going to negatively affect one’s performance.  
:diamonds:	Consensus building is tough because people give weightage to the points that suits their prejudices.
""")

    st.markdown("""After the fall of casual approach, Miss X decides to go with the
                **statistical approach**. From the H.R. department she gets compiled the 
                following data and resorts to statistical methods to analyse the same.""")
    st.markdown("""The features of the data are as follows:    
                **Age**: Age of the concerned employee.    
                **In_time**: Average office in-time.    
                **Work_hrs**: Average working hours.   
                **Duration**: Service duration in months.  
                **Rating**: Average client rating.  
                **Deals**: Average numbers of deals closed per month.  
                **Issues**: Average numbers of issues raised per month.  
                **Leaves**: Average numbers of leaves taken per month.
                
                """)
    import pandas as pd
    df=pd.read_csv("C:\\Users\\Miles\\Documents\\Statistics_streamlit\\Employee.csv")
    st.dataframe(df)
    
    st.markdown("""At first the pool of numbers might seem scary, but it hides a bunch of objective answers to a lot of subjective questions. With some very easy to use tools of statistics following analysis can be done:  
:diamonds:	**Punctuality**: ‘Average reporting time’ and ‘Average working hours’ can be used to compare the punctuality for both the age groups.   
:diamonds:	**Quality of service**: ‘Average client rating’ would provide insights on quality.  
:diamonds:	**Quantity of service**: ‘Deals locked per month' would provide insights on the quantity of work done.  
:diamonds:	**Self-dependence**: ‘Issues raised per month’ would provide some idea about the self-dependence of the employee.  
:diamonds:	**Attrition rate**: Historic data of ‘Months of service’ can give some idea about the attrition rate in both the age groups.  
Based on the importance that the company attaches to each of these metrices, 
Miss X can trade-off between these and make a more informed and harmonious decision. 
                """)
    st.caption(" The exact aggregation methods to be used here will be discussed in the forthcoming chapters.")
    
    with st.expander(":dart: Check the assumptions that can be tested to some extent, with the table shown above."):
        with st.form('1'):
            c1=st.checkbox('Employees who work more, prefer to resolve their issues themselves.')
            c2=st.checkbox('Employees who work more, have lesser quality in their work.')
            c3=st.checkbox('Female employees are more punctual.')
            c4=st.checkbox('Older employees take more leaves.')
            submitted=st.form_submit_button('Submit answers.')
            if submitted==True:
                if c1==True and c2==True and c3==False and c4==True:
                    st.markdown(":large_green_circle: _That's right._")
                elif c3==True:
                    st.markdown(""":large_orange_circle: _Wrong answer. Please pay attention.   
                                Gender data is not provided in the table, so there is no way to check which gender is more punctual_""")
                else:
                    st.markdown(""":large_orange_circle: _Wrong answer.   
                                First assumption can be tested with 'Deals locked' and 'Issues raised'.   
                                Second can be tested with 'Deals locked' and 'Avg client rating'.  
                                Third cannot be tested as gender data is not available.  
                                Fourth can be tested with 'Age' and 'Avg leaves'_""")
    st.markdown(':thumbsdown: **Limitations of Statistics**')
    st.markdown(''':diamonds: Getting a clean, organized, error-free data is a rare occurrence because data collection generally involves human at different stages and humans are not as consistent and error-free as machines.  
:diamonds: Statistics has not been yet proven to be very useful for taking personal decisions e.g. if person A should marry person B or not. The human emotions that are dominantly deterministic to such decisions are yet to be gauged.  
''')
    st.caption("There are some model specific and tool specific limitations that is mentioned alongwith the relevant content in the upcoming topics.")
    with st.expander(':dart: Test your understanding'):
        q3= st.radio('In which of the following situations would you likely **not** use statistical solution?',
                     ['To predict rainfall','To inspect sales','To compare literacy of two regions', 'To compare sorrow of two patients'],index=None,horizontal=True)
        if q3=='To compare sorrow of two patients':
            st.markdown(":large_green_circle: _That's right. Sorrow does not have a number associated with it._")
        elif q3=="To predict rainfall" or q3=="To inspect sales" or q3=="To compare literacy of two regions":
            st.markdown(":large_orange_circle: _Wrong answer. Statistics is already being used for predicting rainfall, inspecting sales, or comparing regions on social indicators like literacy, but sorrow cannot be quantified with a number and hence cannot be dealt with statistics._")
            
elif unit1==  'Presenting Different Types of Data':  
    st.markdown('1. Introduction to Statistics')
    st.subheader("1.2 Presenting Different Types of Data")
    st.divider()

elif unit1==  'Primary Data and Secondary Data':  
    st.markdown('1. Introduction to Statistics')
    st.subheader("1.3 Primary Data and Secondary Data")
    st.divider()
    
elif unit1==  'The Numeric Data and Categorical Data':  
    st.markdown('1. Introduction to Statistics')
    st.subheader("1.4 The Numeric Data and Categorical Data")
    st.divider()
    
elif unit1==  'Continuous Frequency Distribution':  
    st.markdown('1. Introduction to Statistics')
    st.subheader("1.5 Continuous Frequency Distribution")
    st.divider()
    
elif unit1==  'Statistical Analysis with M.S. Excel':  
    st.markdown('1. Introduction to Statistics')
    st.subheader("1.6 Statistical Analysis with M.S. Excel")
    st.divider()
    
# unit 1 over
    
elif unit2== "Central Tendency – Mean, Median and Mode":
    st.markdown('2. Descriptive Statistical Analytics')
    st.subheader("2.1 Central Tendency – Mean, Median and Mode")
    st.divider()
    
elif unit2== "Variance and Standard Deviation":
    st.markdown('2. Descriptive Statistical Analytics')
    st.subheader("2.2 Variance and Standard Deviation")
    st.divider()

elif unit2== "The Coefficient of Variation measures":
    st.markdown('2. Descriptive Statistical Analytics')
    st.subheader("2.3 The Coefficient of Variation measures")
    st.divider()
    
elif unit2== "Measure of Skewness":
    st.markdown('2. Descriptive Statistical Analytics')
    st.subheader("2.4 Measure of Skewness")
    st.divider()
    
elif unit2== "Symmetrical Distribution - Kurtosis":
    st.markdown('2. Descriptive Statistical Analytics')
    st.subheader("2.5 Symmetrical Distribution - Kurtosis")
    st.divider()
    
elif unit2== "Univariate, Bivariate and Multivariate Analysis":
    st.markdown('2. Descriptive Statistical Analytics')
    st.subheader("2.6 Univariate, Bivariate and Multivariate Analysis")
    st.divider()
    
# unit 2 over
    
elif unit3=="Probability Theory":
    st.markdown("3. Probability Theory & Distributions")
    st.subheader("3.1 Probability Theory")
    st.divider()
    
elif unit3=="Fundamental Concepts of Probability":
    st.markdown("3. Probability Theory & Distributions")
    st.subheader("3.2 Fundamental Concepts of Probability")
    st.divider()
    
elif unit3=="Definitions of Probability":
    st.markdown("3. Probability Theory & Distributions")
    st.subheader("3.3 Definitions of Probability")
    st.divider()
    
elif unit3=="Applying Laws of Probability - Bayes Theorem":
    st.markdown("3. Probability Theory & Distributions")
    st.subheader("3.4 Applying Laws of Probability - Bayes Theorem")
    st.divider()
    
elif unit3=="Calculating Random Variable":
    st.markdown("3. Probability Theory & Distributions")
    st.subheader("3.5 Calculating Random Variable")
    st.divider()
    
elif unit3=="Probability-Distribution with a Case Study":
    st.markdown("3. Probability Theory & Distributions")
    st.subheader("3.6 Probability-Distribution with a Case Study")
    st.divider()
    
# unit 3 over 

elif unit4== "Introduction to Sampling Theory":
    st.markdown("4. Sampling and Confidence intervals")
    st.subheader("4.1 Introduction to Sampling Theory")
    st.divider()
    
elif unit4== "Sampling Distribution":
    st.markdown("4. Sampling and Confidence intervals")
    st.subheader("4.2 Sampling Distribution")
    st.divider()
    
elif unit4== "Using probabilistic Sampling Techniques":
    st.markdown("4. Sampling and Confidence intervals")
    st.subheader("4.3 Using probabilistic Sampling Techniques")
    st.divider()
    
elif unit4== "Estimating Sampling Errors":
    st.markdown("4. Sampling and Confidence intervals")
    st.subheader("4.4 Estimating Sampling Errors")
    st.divider()
    
elif unit4== "Confidence Intervals":
    st.markdown("4. Sampling and Confidence intervals")
    st.subheader("4.5 Confidence Intervals")
    st.divider()
    
elif unit4== "Sampling Error and Non-Sampling Error":
    st.markdown("4. Sampling and Confidence intervals")
    st.subheader("4.6 Sampling Error and Non-Sampling Error")
    st.divider()
    
elif unit4== "Central Limit Theorem":
    st.markdown("4. Sampling and Confidence intervals")
    st.subheader("4.7 Central Limit Theorem")
    st.divider()
    
elif unit4== "Case Study on Sampling Techniques":
    st.markdown("4. Sampling and Confidence intervals")
    st.subheader("4.8 Case Study on Sampling Techniques")
    st.divider()
    
# unit 4 over

elif unit5=="Null Hypothesis and Alternate Hypothesis":
    st.markdown("5. Hypothesis testing")
    st.subheader("5.1 Null Hypothesis and Alternate Hypothesis")
    st.divider()
    
elif unit5=="Testing Hypothesis for Large Samples":
    st.markdown("5. Hypothesis testing")
    st.subheader("5.2 Testing Hypothesis for Large Samples")
    st.divider()
    
elif unit5=="Test for Single Proportion":
    st.markdown("5. Hypothesis testing")
    st.subheader("5.3 Test for Single Proportion")
    st.divider()
    
elif unit5=="Test for Difference of Proportions":
    st.markdown("5. Hypothesis testing")
    st.subheader("5.4 Test for Difference of Proportions")
    st.divider()
    
elif unit5=="Testing Hypothesis for Small Samples - T-test":
    st.markdown("5. Hypothesis testing")
    st.subheader("5.5 Testing Hypothesis for Small Samples - T-test")
    st.divider()
    
elif unit5=="Applications of T-test - P-test":
    st.markdown("5. Hypothesis testing")
    st.subheader("5.6 Applications of T-test - P-test")
    st.divider()
    
elif unit5=="Two-Way Factorial ANOVA":
    st.markdown("5. Hypothesis testing")
    st.subheader("5.7 Two-Way Factorial ANOVA")
    st.divider()
    
elif unit5=="Chi-Square Test and its Application":
    st.markdown("5. Hypothesis testing")
    st.subheader("5.8 Chi-Square Test and its Application")
    st.divider()
    
elif unit5=="Testing the Goodness of Fit":
    st.markdown("5. Hypothesis testing")
    st.subheader("5.9 Testing the Goodness of Fit")
    st.divider()
    
elif unit5=="Case Study on Hypothesis Testing with Excel":
    st.markdown("5. Hypothesis testing")
    st.subheader("5.10 Case Study on Hypothesis Testing with Excel")
    st.divider()
    