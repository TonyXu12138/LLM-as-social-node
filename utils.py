import re

# ###1. Class
# class_3_lst = [
#     ("Class","Solver", "Takes the lead in solving the problem step-by-step and explains their reasoning clearly.", 1),
#     ("Class","Critic", "Challenges the Solver's solution by identifying errors, questioning assumptions, and suggesting improvements or alternative approaches.", 1),
#     ("Class","Coordinator", "Mediates discussions, keeps the group organized, ensures productive dialogue, and synthesizes contributions into a cohesive solution.", 1)
# ]

# class_6_lst = [
#     ("Class","Solver", "Takes charge of solving the main problem or its most critical part, breaking it down systematically.", 1),
#     ("Class","Solver", "Supports the main Solver by working on complementary subproblems or calculations.", 2),
#     ("Class","Critic", "Reviews the first Solver's work for errors, logical gaps, or unclear reasoning.", 1),
#     ("Class","Critic", "Reviews the second Solver's work or checks alternative approaches to ensure robustness.", 2),
#     ("Class","Strategist", "Proposes an overall plan or framework for solving the problem, assigns tasks, and ensures efficient collaboration.", 1),
#     ("Class","Coordinator", "Mediates discussions, organizes contributions, resolves disputes, and synthesizes the group’s work into a cohesive solution.", 1)
# ]

# ###2. Finance
# Fina_6_lst = [
#     ("Finance", "Analyst", "Extract relevant data from financial text", 1),
#     ("Finance", "Data Scientist", "Parse and interpret table data", 1),
#     ("Finance", "Accountant", "Perform calculations based on given data", 1),
#     ("Finance", "Manager", "Verify the consistency of extracted data", 1),
#     ("Finance", "Strategist", "Synthesize findings into a coherent answer", 1),
#     ("Finance", "Evaluator", "Validate the final answer and reasoning", 1)
# ]

# Fina_10_lst = [
#     ("Finance", "Analyst", "Extract data from financial text", 1),
#     ("Finance", "Analyst", "Extract additional relevant data from text", 2),
#     ("Finance", "Data Scientist", "Extract and interpret table data", 1),
#     ("Finance", "Data Scientist", "Cross-check table data and identify patterns", 2),
#     ("Finance", "Accountant", "Perform calculations (e.g., sums, ratios)", 1),
#     ("Finance", "Accountant", "Perform advanced calculations (e.g., percentages)", 2),
#     ("Finance", "Auditor", "Validate data consistency across sources", 1),
#     ("Finance", "Strategist", "Synthesize findings into a coherent draft answer", 1),
#     ("Finance", "Manager", "Cross-check the synthesized reasoning", 1),
#     ("Finance", "Evaluator", "Validate the final answer and provide feedback", 1)
# ]

# Fina_20_lst = [
#     ("Finance", "Analyst", "Extract financial data from the text", 1),
#     ("Finance", "Analyst", "Extract additional financial data from the text", 2),
#     ("Finance", "Analyst", "Identify key metrics in the financial context", 3),
#     ("Finance", "Analyst", "Highlight any ambiguous or missing data", 4),
#     ("Finance", "Data Scientist", "Extract and process table data", 1),
#     ("Finance", "Data Scientist", "Cross-check table data for errors or omissions", 2),
#     ("Finance", "Data Scientist", "Identify trends or patterns in numerical data", 3),
#     ("Finance", "Data Scientist", "Confirm relevance of table data to the question", 4),
#     ("Finance", "Accountant", "Perform basic calculations (e.g., sums, ratios)", 1),
#     ("Finance", "Accountant", "Perform advanced calculations (e.g., growth rates)", 2),
#     ("Finance", "Accountant", "Break down complex calculations into smaller steps", 3),
#     ("Finance", "Accountant", "Validate all calculations for accuracy", 4),
#     ("Finance", "Auditor", "Ensure consistency between text, table, and calculations", 1),
#     ("Finance", "Auditor", "Identify potential discrepancies in data sources", 2),
#     ("Finance", "Strategist", "Synthesize findings into an answer draft", 1),
#     ("Finance", "Strategist", "Add supporting reasoning to the draft", 2),
#     ("Finance", "Manager", "Review the synthesis and ensure logical flow", 1),
#     ("Finance", "Manager", "Propose alternative answers if inconsistencies arise", 2),
#     ("Finance", "Evaluator", "Validate the final answer and reasoning", 1),
#     ("Finance", "Evaluator", "Provide a final confidence score for the answer", 2)
# ]


# ###3. Medicine
# med_6_lst = [
#     ('hospital', 'Doctor', 'Diagnose and treat patients based on symptoms and medical history', 1),
#     ('hospital', 'Nurse', 'Provide bedside care, administer medications, and monitor patient conditions', 1),
#     ('hospital', 'Pharmacist', 'Prepare and dispense medications based on prescriptions and advise on drug interactions', 1),
#     ('hospital', 'Receptionist', 'Manage appointments, patient records, and communication between departments', 1),
#     ('hospital', 'Medical Lab Technician', 'Perform diagnostic tests and analyze lab results for patient treatment', 1),
#     ('hospital', 'Surgeon', 'Perform surgical procedures and collaborate with the medical team on treatment plans', 1),
# ]

# med_10_lst = [
#     ('hospital', 'Doctor', 'Diagnose and treat patients based on symptoms and medical history', 1),
#     ('hospital', 'Doctor', 'Focus on specialized care, such as cardiology or pediatrics', 2),
#     ('hospital', 'Nurse', 'Provide bedside care, administer medications, and monitor patient conditions', 1),
#     ('hospital', 'Nurse', 'Assist in emergency care and prepare patients for procedures', 2),
#     ('hospital', 'Pharmacist', 'Prepare and dispense medications based on prescriptions and advise on drug interactions', 1),
#     ('hospital', 'Receptionist', 'Manage appointments, patient records, and communication between departments', 1),
#     ('hospital', 'Medical Lab Technician', 'Perform diagnostic tests and analyze lab results for patient treatment', 1),
#     ('hospital', 'Surgeon', 'Perform surgical procedures and collaborate with the medical team on treatment plans', 1),
#     ('hospital', 'Radiologist', 'Analyze medical imaging to assist in diagnosis and treatment', 1),
#     ('hospital', 'Physiotherapist', 'Develop rehabilitation plans to improve patient mobility and strength', 1),
# ]

# med_20_lst =  [
#     ('hospital', 'Doctor', 'Diagnose and treat patients based on symptoms and medical history', 1),
#     ('hospital', 'Doctor', 'Focus on specialized care, such as cardiology or pediatrics', 2),
#     ('hospital', 'Doctor', 'Oversee patient care and collaborate with other specialists', 3),
#     ('hospital', 'Nurse', 'Provide bedside care, administer medications, and monitor patient conditions', 1),
#     ('hospital', 'Nurse', 'Assist in emergency care and prepare patients for procedures', 2),
#     ('hospital', 'Nurse', 'Support surgeries and provide post-operative care', 3),
#     ('hospital', 'Pharmacist', 'Prepare and dispense medications based on prescriptions and advise on drug interactions', 1),
#     ('hospital', 'Pharmacist', 'Monitor medication usage and educate staff about new drugs', 2),
#     ('hospital', 'Receptionist', 'Manage appointments, patient records, and communication between departments', 1),
#     ('hospital', 'Receptionist', 'Handle patient inquiries and ensure smooth coordination between departments', 2),
#     ('hospital', 'Medical Lab Technician', 'Perform diagnostic tests and analyze lab results for patient treatment', 1),
#     ('hospital', 'Medical Lab Technician', 'Maintain lab equipment and ensure accurate test results', 2),
#     ('hospital', 'Surgeon', 'Perform surgical procedures and collaborate with the medical team on treatment plans', 1),
#     ('hospital', 'Surgeon', 'Specialize in minimally invasive or emergency surgeries', 2),
#     ('hospital', 'Radiologist', 'Analyze medical imaging to assist in diagnosis and treatment', 1),
#     ('hospital', 'Radiologist', 'Collaborate with other specialists to interpret imaging results', 2),
#     ('hospital', 'Physiotherapist', 'Develop rehabilitation plans to improve patient mobility and strength', 1),
#     ('hospital', 'Physiotherapist', 'Assist patients recovering from surgeries or injuries', 2),
#     ('hospital', 'Psychologist', 'Provide mental health support and therapy for patients', 1),
#     ('hospital', 'Psychologist', 'Conduct psychological evaluations and support staff mental health', 2),
# ]

# ###4. Law
# law_6_lst = [
#     ('law', 'Judge', 'Preside over court proceedings, interpret the law, and make rulings', 1),
#     ('law', 'Prosecutor', 'Represent the state and present evidence against the defendant', 1),
#     ('law', 'Defense Attorney', 'Represent the defendant and provide legal defense', 1),
#     ('law', 'Court Clerk', 'Maintain court records, manage schedules, and assist the judge', 1),
#     ('law', 'Legal Researcher', 'Conduct research on legal precedents, statutes, and case law', 1),
#     ('law', 'Witness', 'Provide testimony based on their knowledge or experience relevant to the case', 1),
# ]

# legal_6_lst = [
#     ('legal', 'Judge', 'Oversees court proceedings and ensures fair trials', '1'),
#     ('legal', 'Attorney', 'Represents clients in legal matters', '1'),
#     ('legal', 'Attorney', 'Represents clients in legal matters', '2'),
#     ('legal', 'Paralegal', 'Assists attorneys with legal research and documentation', '1'),
#     ('legal', 'Clerk', 'Manages court records and documents', '1'),
#     ('legal', 'Bailiff', 'Maintains order in the courtroom', '1'),
# ]

# law_10_lst =[
#     ('law', 'Judge', 'Preside over court proceedings, interpret the law, and make rulings', 1),
#     ('law', 'Judge', 'Focus on ensuring due process and a fair trial', 2),
#     ('law', 'Prosecutor', 'Represent the state and present evidence against the defendant', 1),
#     ('law', 'Prosecutor', 'Handle cross-examinations and rebuttals', 2),
#     ('law', 'Defense Attorney', 'Represent the defendant and provide legal defense', 1),
#     ('law', 'Defense Attorney', 'Focus on legal arguments and challenging evidence', 2),
#     ('law', 'Court Clerk', 'Maintain court records, manage schedules, and assist the judge', 1),
#     ('law', 'Legal Researcher', 'Conduct research on legal precedents, statutes, and case law', 1),
#     ('law', 'Paralegal', 'Support attorneys by drafting documents and preparing case files', 1),
#     ('law', 'Witness', 'Provide testimony based on their knowledge or experience relevant to the case', 1),
# ]

# law_20_lst = [
#     ('law', 'Judge', 'Preside over court proceedings, interpret the law, and make rulings', 1),
#     ('law', 'Judge', 'Ensure fair procedures and adherence to legal standards', 2),
#     ('law', 'Judge', 'Specialize in mediation and arbitration for resolving disputes', 3),
#     ('law', 'Prosecutor', 'Represent the state and present evidence against the defendant', 1),
#     ('law', 'Prosecutor', 'Handle witness examinations and closing arguments', 2),
#     ('law', 'Prosecutor', 'Focus on building a strong case using evidence and legal precedents', 3),
#     ('law', 'Defense Attorney', 'Represent the defendant and provide legal defense', 1),
#     ('law', 'Defense Attorney', 'Challenge the admissibility of evidence and protect client rights', 2),
#     ('law', 'Defense Attorney', 'Negotiate plea bargains or settlements', 3),
#     ('law', 'Court Clerk', 'Maintain court records, manage schedules, and assist the judge', 1),
#     ('law', 'Court Clerk', 'Coordinate communication between parties and manage documentation', 2),
#     ('law', 'Legal Researcher', 'Conduct research on legal precedents, statutes, and case law', 1),
#     ('law', 'Legal Researcher', 'Provide detailed legal memos to assist attorneys and judges', 2),
#     ('law', 'Paralegal', 'Support attorneys by drafting documents and preparing case files', 1),
#     ('law', 'Paralegal', 'Organize evidence and assist during trials or hearings', 2),
#     ('law', 'Witness', 'Provide testimony based on their knowledge or experience relevant to the case', 1),
#     ('law', 'Expert Witness', 'Offer specialized knowledge or opinions relevant to the case', 1),
#     ('law', 'Expert Witness', 'Provide technical or medical insights to clarify evidence', 2),
#     ('law', 'Bailiff', 'Ensure security and order in the courtroom', 1),
#     ('law', 'Mediator', 'Facilitate negotiations and settlements between disputing parties', 1),
# ]


# #5. Journalism
# journalism_6_lst = [
#     ('journalism', 'Editor', 'Oversee content and ensure quality', 1),
#     ('journalism', 'Reporter', 'Investigate and report stories', 1),
#     ('journalism', 'Photographer', 'Capture photos related to news stories', 1),
#     ('journalism', 'Videographer', 'Film and edit video content', 1),
#     ('journalism', 'Fact-Checker', 'Verify the accuracy of information', 1),
#     ('journalism', 'Publisher', 'Distribute the final product to the audience', 1),
# ]

# journalism_10_lst = [
#     ('journalism', 'Editor', 'Oversee content and ensure quality', 1),
#     ('journalism', 'Assistant Editor', 'Assist the editor and manage smaller sections', 1),
#     ('journalism', 'Reporter', 'Investigate and report stories', 1),
#     ('journalism', 'Reporter', 'Focus on special-interest topics or breaking news', 2),
#     ('journalism', 'Photographer', 'Capture photos related to news stories', 1),
#     ('journalism', 'Videographer', 'Film and edit video content', 1),
#     ('journalism', 'Fact-Checker', 'Verify the accuracy of information', 1),
#     ('journalism', 'Publisher', 'Distribute the final product to the audience', 1),
#     ('journalism', 'Social Media Manager', 'Promote content on social media platforms', 1),
#     ('journalism', 'Data Journalist', 'Analyze and visualize data for stories', 1),
# ]

# journalism_20_lst = [
#     ('journalism', 'Editor', 'Oversee content and ensure quality', 1),
#     ('journalism', 'Assistant Editor', 'Assist the editor and manage smaller sections', 1),
#     ('journalism', 'Reporter', 'Investigate and report stories', 1),
#     ('journalism', 'Reporter', 'Focus on special-interest topics or breaking news', 2),
#     ('journalism', 'Reporter', 'Specialize in investigative journalism', 3),
#     ('journalism', 'Photographer', 'Capture photos related to news stories', 1),
#     ('journalism', 'Photographer', 'Specialize in live event photography', 2),
#     ('journalism', 'Videographer', 'Film and edit video content', 1),
#     ('journalism', 'Videographer', 'Focus on documentary-style footage', 2),
#     ('journalism', 'Fact-Checker', 'Verify the accuracy of information', 1),
#     ('journalism', 'Fact-Checker', 'Cross-reference sources for in-depth stories', 2),
#     ('journalism', 'Publisher', 'Distribute the final product to the audience', 1),
#     ('journalism', 'Social Media Manager', 'Promote content on social media platforms', 1),
#     ('journalism', 'Social Media Manager', 'Engage with audiences across networks', 2),
#     ('journalism', 'Data Journalist', 'Analyze and visualize data for stories', 1),
#     ('journalism', 'Illustrator', 'Create visuals and infographics for stories', 1),
#     ('journalism', 'Copy Editor', 'Edit text for grammar, style, and clarity', 1),
#     ('journalism', 'Media Liaison', 'Coordinate interviews and manage press relationships', 1),
#     ('journalism', 'Columnist', 'Write opinion pieces and editorials', 1),
#     ('journalism', 'Ethics Officer', 'Ensure adherence to journalistic integrity', 1),
# ]


# ###6. Disaster Relief###
# disaster_relief_6_lst = [
#     ('disaster', 'Team Leader', 'Coordinate the team and prioritize tasks', 1),
#     ('disaster', 'Medic', 'Provide medical care to injured individuals', 1),
#     ('disaster', 'Rescuer', 'Search for and rescue people in danger', 1),
#     ('disaster', 'Engineer', 'Assess structural damage and recommend repairs', 1),
#     ('disaster', 'Logistics Coordinator', 'Manage supplies and resources', 1),
#     ('disaster', 'Communicator', 'Relay information between the field and command centers', 1),
# ]

# disaster_relief_10_lst = [
#     ('disaster', 'Team Leader', 'Coordinate the team and prioritize tasks', 1),
#     ('disaster', 'Deputy Leader', 'Assist the leader and manage smaller groups', 1),
#     ('disaster', 'Medic', 'Provide medical care to injured individuals', 1),
#     ('disaster', 'Medic', 'Set up temporary medical stations and triage patients', 2),
#     ('disaster', 'Rescuer', 'Search for and rescue people in danger', 1),
#     ('disaster', 'Rescuer', 'Operate rescue equipment and assist evacuation efforts', 2),
#     ('disaster', 'Engineer', 'Assess damage and recommend repairs', 1),
#     ('disaster', 'Logistics Coordinator', 'Manage supplies and resources', 1),
#     ('disaster', 'Communicator', 'Relay information between the field and command centers', 1),
#     ('disaster', 'Data Analyst', 'Compile and analyze data to inform decisions', 1),
# ]

# disaster_relief_20_lst = [
#     ('disaster', 'Team Leader', 'Coordinate the team and prioritize tasks', 1),
#     ('disaster', 'Deputy Leader', 'Assist the leader and manage smaller groups', 1),
#     ('disaster', 'Medic', 'Provide medical care to injured individuals', 1),
#     ('disaster', 'Medic', 'Set up temporary medical stations and triage patients', 2),
#     ('disaster', 'Medic', 'Train volunteers in basic first aid', 3),
#     ('disaster', 'Rescuer', 'Search for and rescue people in danger', 1),
#     ('disaster', 'Rescuer', 'Operate rescue equipment and assist evacuation efforts', 2),
#     ('disaster', 'Rescuer', 'Support underwater or hazardous rescues', 3),
#     ('disaster', 'Engineer', 'Assess damage and recommend repairs', 1),
#     ('disaster', 'Engineer', 'Create temporary infrastructure for relief efforts', 2),
#     ('disaster', 'Logistics Coordinator', 'Manage supplies and resources', 1),
#     ('disaster', 'Logistics Coordinator', 'Oversee transportation of supplies to affected areas', 2),
#     ('disaster', 'Communicator', 'Relay information between the field and command centers', 1),
#     ('disaster', 'Data Analyst', 'Compile and analyze data to inform decisions', 1),
#     ('disaster', 'Safety Officer', 'Monitor and enforce safety protocols', 1),
#     ('disaster', 'Volunteer Coordinator', 'Organize and deploy volunteers to key areas', 1),
#     ('disaster', 'Psychologist', 'Provide mental health support to victims and responders', 1),
#     ('disaster', 'Media Liaison', 'Share updates and coordinate with the media', 1),
#     ('disaster', 'Evaluator', 'Assess the team’s response and recommend improvements', 1),
#     ('disaster', 'Crisis Planner', 'Develop strategies for long-term recovery', 1),
# ]

# ###7. Research Lab###
# research_lab_6_lst = [
#     ('research', 'Principal Investigator', 'Lead the research project and define goals', 1),
#     ('research', 'Research Scientist', 'Conduct experiments and analyze data', 1),
#     ('research', 'Research Scientist', 'Focus on experimental design and protocol', 2),
#     ('research', 'Lab Technician', 'Prepare materials and maintain lab equipment', 1),
#     ('research', 'Data Analyst', 'Analyze experimental results and create reports', 1),
#     ('research', 'Safety Officer', 'Ensure compliance with safety regulations', 1),
# ]

# research_lab_10_lst = [
#     ('research', 'Principal Investigator', 'Lead the research project and define goals', 1),
#     ('research', 'Co-Investigator', 'Assist the PI and coordinate subprojects', 1),
#     ('research', 'Research Scientist', 'Conduct experiments and analyze data', 1),
#     ('research', 'Research Scientist', 'Focus on experimental design and protocol', 2),
#     ('research', 'Research Assistant', 'Support experiments and documentation', 1),
#     ('research', 'Lab Technician', 'Prepare materials and maintain lab equipment', 1),
#     ('research', 'Lab Technician', 'Oversee inventory and calibrate instruments', 2),
#     ('research', 'Data Analyst', 'Analyze experimental results and create reports', 1),
#     ('research', 'Safety Officer', 'Ensure compliance with safety regulations', 1),
#     ('research', 'Grant Writer', 'Prepare grant applications and funding proposals', 1),
# ]

# research_lab_20_lst = [
#     ('research', 'Principal Investigator', 'Lead the research project and define goals', 1),
#     ('research', 'Co-Investigator', 'Assist the PI and coordinate subprojects', 1),
#     ('research', 'Senior Research Scientist', 'Develop methodologies and supervise junior staff', 1),
#     ('research', 'Research Scientist', 'Conduct experiments and analyze data', 1),
#     ('research', 'Research Scientist', 'Focus on experimental design and protocol', 2),
#     ('research', 'Research Assistant', 'Support experiments and documentation', 1),
#     ('research', 'Research Assistant', 'Prepare samples and assist with data collection', 2),
#     ('research', 'Lab Technician', 'Prepare materials and maintain lab equipment', 1),
#     ('research', 'Lab Technician', 'Oversee inventory and calibrate instruments', 2),
#     ('research', 'Data Analyst', 'Analyze experimental results and create reports', 1),
#     ('research', 'Data Analyst', 'Develop data visualization tools and dashboards', 2),
#     ('research', 'Safety Officer', 'Ensure compliance with safety regulations', 1),
#     ('research', 'Safety Officer', 'Train staff on safety procedures', 2),
#     ('research', 'Grant Writer', 'Prepare grant applications and funding proposals', 1),
#     ('research', 'Grant Writer', 'Focus on securing long-term funding opportunities', 2),
#     ('research', 'Statistician', 'Develop statistical models for data analysis', 1),
#     ('research', 'Ethics Officer', 'Ensure experiments follow ethical guidelines', 1),
#     ('research', 'IT Specialist', 'Maintain computational resources and software', 1),
#     ('research', 'Communicator', 'Present research findings to stakeholders', 1),
#     ('research', 'Administrative Assistant', 'Manage schedules, documentation, and logistics', 1),
# ]

# ###8. Event Managemengt
# event_mgmt_6_lst = [
#     ('event', 'Event Manager', 'Plan and oversee the execution of the event', 1),
#     ('event', 'Logistics Manager', 'Coordinate transportation and venue setup', 1),
#     ('event', 'Marketing Specialist', 'Promote the event and manage advertising', 1),
#     ('event', 'Catering Manager', 'Organize food and beverage services', 1),
#     ('event', 'Technical Support', 'Set up and manage audiovisual equipment', 1),
#     ('event', 'Security Officer', 'Ensure safety and manage crowd control', 1),
# ]

# event_mgmt_10_lst = [
#     ('event', 'Event Manager', 'Plan and oversee the execution of the event', 1),
#     ('event', 'Assistant Event Manager', 'Support the Event Manager with coordination tasks', 1),
#     ('event', 'Logistics Manager', 'Coordinate transportation and venue setup', 1),
#     ('event', 'Marketing Specialist', 'Promote the event and manage advertising', 1),
#     ('event', 'Catering Manager', 'Organize food and beverage services', 1),
#     ('event', 'Technical Support', 'Set up and manage audiovisual equipment', 1),
#     ('event', 'Technical Support', 'Troubleshoot technical issues during the event', 2),
#     ('event', 'Security Officer', 'Ensure safety and manage crowd control', 1),
#     ('event', 'Volunteer Coordinator', 'Organize and direct event volunteers', 1),
#     ('event', 'Guest Liaison', 'Assist VIPs and address participant inquiries', 1),
# ]

# event_mgmt_20_lst = [
#     ('event', 'Event Manager', 'Plan and oversee the execution of the event', 1),
#     ('event', 'Assistant Event Manager', 'Support the Event Manager with coordination tasks', 1),
#     ('event', 'Logistics Manager', 'Coordinate transportation and venue setup', 1),
#     ('event', 'Logistics Manager', 'Oversee storage and transport of materials', 2),
#     ('event', 'Marketing Specialist', 'Promote the event and manage advertising', 1),
#     ('event', 'Marketing Specialist', 'Manage social media campaigns and updates', 2),
#     ('event', 'Catering Manager', 'Organize food and beverage services', 1),
#     ('event', 'Catering Manager', 'Ensure dietary requirements are met', 2),
#     ('event', 'Technical Support', 'Set up and manage audiovisual equipment', 1),
#     ('event', 'Technical Support', 'Troubleshoot technical issues during the event', 2),
#     ('event', 'Security Officer', 'Ensure safety and manage crowd control', 1),
#     ('event', 'Security Officer', 'Monitor entry points and enforce protocols', 2),
#     ('event', 'Volunteer Coordinator', 'Organize and direct event volunteers', 1),
#     ('event', 'Volunteer Coordinator', 'Assign tasks and manage volunteer schedules', 2),
#     ('event', 'Guest Liaison', 'Assist VIPs and address participant inquiries', 1),
#     ('event', 'Guest Liaison', 'Resolve guest complaints and ensure satisfaction', 2),
#     ('event', 'Stage Manager', 'Coordinate activities on stage during the event', 1),
#     ('event', 'Photographer', 'Capture key moments and highlights', 1),
#     ('event', 'Decorator', 'Design and decorate the venue', 1),
#     ('event', 'Cleaner', 'Ensure the venue is clean before and after the event', 1),
# ]

# ###9. Construction Project###
# construction_6_lst = [
#     ('construction', 'Project Manager', 'Oversee the construction project and ensure timely completion', 1),
#     ('construction', 'Engineer', 'Design and oversee technical aspects of the project', 1),
#     ('construction', 'Site Supervisor', 'Manage on-site workers and resources', 1),
#     ('construction', 'Architect', 'Create and finalize building designs', 1),
#     ('construction', 'Safety Officer', 'Ensure compliance with safety regulations', 1),
#     ('construction', 'Laborer', 'Perform construction tasks and assist specialists', 1),
# ]

# construction_10_lst = [
#     ('construction', 'Project Manager', 'Oversee the construction project and ensure timely completion', 1),
#     ('construction', 'Assistant Project Manager', 'Support the Project Manager with coordination', 1),
#     ('construction', 'Engineer', 'Design and oversee technical aspects of the project', 1),
#     ('construction', 'Engineer', 'Focus on structural integrity and geotechnical analysis', 2),
#     ('construction', 'Site Supervisor', 'Manage on-site workers and resources', 1),
#     ('construction', 'Site Supervisor', 'Handle scheduling and resource tracking', 2),
#     ('construction', 'Architect', 'Create and finalize building designs', 1),
#     ('construction', 'Safety Officer', 'Ensure compliance with safety regulations', 1),
#     ('construction', 'Laborer', 'Perform construction tasks and assist specialists', 1),
#     ('construction', 'Foreman', 'Direct and oversee the work of labor crews', 1),
# ]

# construction_20_lst = [
#     ('construction', 'Project Manager', 'Oversee the construction project and ensure timely completion', 1),
#     ('construction', 'Assistant Project Manager', 'Support the Project Manager with coordination', 1),
#     ('construction', 'Engineer', 'Design and oversee technical aspects of the project', 1),
#     ('construction', 'Engineer', 'Focus on structural integrity and geotechnical analysis', 2),
#     ('construction', 'Engineer', 'Develop HVAC and plumbing systems for the project', 3),
#     ('construction', 'Site Supervisor', 'Manage on-site workers and resources', 1),
#     ('construction', 'Site Supervisor', 'Handle scheduling and resource tracking', 2),
#     ('construction', 'Architect', 'Create and finalize building designs', 1),
#     ('construction', 'Architect', 'Focus on aesthetics and interior planning', 2),
#     ('construction', 'Safety Officer', 'Ensure compliance with safety regulations', 1),
#     ('construction', 'Safety Officer', 'Conduct safety training for workers', 2),
#     ('construction', 'Laborer', 'Perform construction tasks and assist specialists', 1),
#     ('construction', 'Laborer', 'Transport materials and prepare tools', 2),
#     ('construction', 'Foreman', 'Direct and oversee the work of labor crews', 1),
#     ('construction', 'Electrician', 'Install and maintain electrical systems', 1),
#     ('construction', 'Plumber', 'Install and repair water systems and pipes', 1),
#     ('construction', 'Heavy Equipment Operator', 'Operate machinery like cranes and excavators', 1),
#     ('construction', 'Quality Inspector', 'Inspect work to ensure it meets standards', 1),
#     ('construction', 'Planner', 'Create and manage construction schedules', 1),
#     ('construction', 'Surveyor', 'Measure and map the construction site', 1),
# ]

# ###10. Emergency Response
# emergency_response_6_lst = [
#     ('emergency', 'Team Leader', 'Coordinate the team and allocate resources', 1),
#     ('emergency', 'Paramedic', 'Provide medical care to victims', 1),
#     ('emergency', 'Firefighter', 'Control fires and rescue victims', 1),
#     ('emergency', 'Search Specialist', 'Search for trapped or missing individuals', 1),
#     ('emergency', 'Logistics Officer', 'Manage supplies and equipment', 1),
#     ('emergency', 'Communicator', 'Relay information between teams and authorities', 1),
# ]

# emergency_response_10_lst = [
#     ('emergency', 'Team Leader', 'Coordinate the team and allocate resources', 1),
#     ('emergency', 'Deputy Team Leader', 'Assist the leader and oversee sub-teams', 1),
#     ('emergency', 'Paramedic', 'Provide medical care to victims', 1),
#     ('emergency', 'Paramedic', 'Set up triage stations and prioritize care', 2),
#     ('emergency', 'Firefighter', 'Control fires and rescue victims', 1),
#     ('emergency', 'Search Specialist', 'Search for trapped or missing individuals', 1),
#     ('emergency', 'Search Specialist', 'Operate search equipment like drones', 2),
#     ('emergency', 'Logistics Officer', 'Manage supplies and equipment', 1),
#     ('emergency', 'Communicator', 'Relay information between teams and authorities', 1),
#     ('emergency', 'Safety Officer', 'Ensure team safety and adherence to protocols', 1),
# ]

# emergency_response_20_lst = [
#     ('emergency', 'Team Leader', 'Coordinate the team and allocate resources', 1),
#     ('emergency', 'Deputy Team Leader', 'Assist the leader and oversee sub-teams', 1),
#     ('emergency', 'Paramedic', 'Provide medical care to victims', 1),
#     ('emergency', 'Paramedic', 'Set up triage stations and prioritize care', 2),
#     ('emergency', 'Paramedic', 'Train volunteers in first aid', 3),
#     ('emergency', 'Firefighter', 'Control fires and rescue victims', 1),
#     ('emergency', 'Firefighter', 'Focus on hazardous materials incidents', 2),
#     ('emergency', 'Search Specialist', 'Search for trapped or missing individuals', 1),
#     ('emergency', 'Search Specialist', 'Operate search equipment like drones', 2),
#     ('emergency', 'Search Specialist', 'Focus on underwater or confined space rescues', 3),
#     ('emergency', 'Logistics Officer', 'Manage supplies and equipment', 1),
#     ('emergency', 'Logistics Officer', 'Coordinate supply transport to the site', 2),
#     ('emergency', 'Communicator', 'Relay information between teams and authorities', 1),
#     ('emergency', 'Communicator', 'Draft public safety announcements', 2),
#     ('emergency', 'Safety Officer', 'Ensure team safety and adherence to protocols', 1),
#     ('emergency', 'Safety Officer', 'Conduct on-site safety assessments', 2),
#     ('emergency', 'Data Analyst', 'Analyze data to optimize response efforts', 1),
#     ('emergency', 'Planner', 'Create schedules and track progress', 1),
#     ('emergency', 'Psychologist', 'Support the mental health of victims and responders', 1),
#     ('emergency', 'Media Liaison', 'Handle press inquiries and public updates', 1),
# ]

# #11. education
# edu_6_lst = [
# ('education', 'Professor', 'Teaches advanced topics and conducts research', '1'),
# ('education', 'Lecturer', 'Delivers lectures on various subjects', '1'),
# ('education', 'Teaching Assistant', 'Supports lecturers and helps students', '1'),
# ('education', 'Student', 'Learns and participates in coursework', '1'),
# ('education', 'Student', 'Learns and participates in coursework', '2'),
# ('education', 'Administrator', 'Manages academic operations', '1'),
# ]

# edu_10_lst = [
# ('math', 'Mathematician', 'Conducts research and develops mathematical theories', '1'),
# ('math', 'Mathematician', 'Conducts research and develops mathematical theories', '2'),
# ('math', 'Professor', 'Teaches mathematical concepts and mentors students', '1'),
# ('math', 'Professor', 'Teaches mathematical concepts and mentors students', '2'),
# ('math', 'Lecturer', 'Delivers courses on applied and pure mathematics', '1'),
# ('math', 'Teaching Assistant', 'Assists in grading and tutoring students', '1'),
# ('math', 'Teaching Assistant', 'Assists in grading and tutoring students', '2'),
# ('math', 'Student', 'Studies mathematical theories and applications', '1'),
# ('math', 'Student', 'Studies mathematical theories and applications', '2'),
# ('math', 'Researcher', 'Works on mathematical models and problem-solving', '1'),
# ]

# edu_20_lst = [
# ('education', 'Dean', 'Oversees the academic and administrative functions of a faculty', '1'),
# ('education', 'Professor', 'Teaches advanced topics and supervises research', '1'),
# ('education', 'Professor', 'Teaches advanced topics and supervises research', '2'),
# ('education', 'Lecturer', 'Delivers lectures in various subjects', '1'),
# ('education', 'Lecturer', 'Delivers lectures in various subjects', '2'),
# ('education', 'Teaching Assistant', 'Supports lecturers and helps students', '1'),
# ('education', 'Teaching Assistant', 'Supports lecturers and helps students', '2'),
# ('education', 'Administrator', 'Manages academic operations', '1'),
# ('education', 'Administrator', 'Manages academic operations', '2'),
# ('math', 'Mathematician', 'Develops and proves mathematical theorems', '1'),
# ('math', 'Mathematician', 'Develops and proves mathematical theorems', '2'),
# ('math', 'Mathematician', 'Develops and proves mathematical theorems', '3'),
# ('math', 'Professor', 'Teaches mathematical concepts and supervises research', '1'),
# ('math', 'Professor', 'Teaches mathematical concepts and supervises research', '2'),
# ('math', 'Researcher', 'Works on mathematical models and computation', '1'),
# ('math', 'Researcher', 'Works on mathematical models and computation', '2'),
# ('math', 'Student', 'Studies mathematical theories and applications', '1'),
# ('math', 'Student', 'Studies mathematical theories and applications', '2'),
# ('math', 'Student', 'Studies mathematical theories and applications', '3'),
# ('math', 'Curriculum Developer', 'Designs educational programs and materials', '1'),
# ]


###Functions
def generate_template(role_resp_lst,message_hist, turn, problem, mode = 'RR'):
    #given the history and the role responsibility, generate the message to be fed into the model
    #message user, should say something different to others, further development should be tested later.
    if mode == 'RR':
        role_info = role_resp_lst[turn % len(role_resp_lst)]
        # system_info = f'You are a {role_info[1].lower()} in a {role_info[0].lower()}. You are about to solve a problem in the {role_info[0].lower()}, your role in the discussion is {role_info[2].lower()} and your responsibility is to {role_info[3].lower()}'
        # system_info = f'You are a {role_info[1].lower()} in a {role_info[0].lower()} domain. You are about to solve a problem in the {role_info[0].lower()} domain, your responsibility is to {role_info[2].lower()}'
        # messages = [
        #     {"role": "system", "content": system_info},
        #     {"role": "user", "content": message_hist + '\n'+ f'Again, the problem is {problem}, according to your role and responsibility, please give your idea to the problem to the discussion. In the end, please remember to output the answer index in \\boxed{{}}. Please limit the final output length within 150 words.'},
        # ]
        
        # Extract role information with clear variable names
        domain = role_info[0].lower()       # Field/domain of expertise 
        title = role_info[1].lower()        # Professional title
        duty = role_info[2].lower()         # Professional responsibility

        # System message with explicit role framing
        system_prompt = f'''[ROLE ASSIGNMENT]
        You are a {title} specializing in {domain}.
        Your professional responsibility is to {duty}.

        IMPORTANT: Think and respond EXACTLY as a real {title} in {domain} would.
        Use terminology, methods, and perspectives specific to your professional field.'''

        # User message with clear structure and requirements
        user_prompt = f'''Previous discussion:
        {message_hist}

        PROBLEM TO SOLVE:
        {problem}

        RESPONSE INSTRUCTIONS:
        1. Begin with: "As a {title} in {domain}, I..."
        2. Analyze the problem using your professional expertise
        3. Provide your expert recommendation
        4. End with: "My answer is \\boxed{{X}}" where X is the answer index

        REQUIREMENTS:
        - Maintain your {title} perspective throughout
        - Use terminology from {domain}
        - Keep response under 150 words
        - Your answer MUST be in \\boxed{{}} format

        Remember: You are a {title}, not an AI assistant. Think and respond accordingly.'''

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

    return messages 

def answer_extraction(text):
    # Regular expression to match the content inside \boxed{}
    match = re.search(r"\\boxed\{(.*?)\}", text)

    if match:
        answer = match.group(1)  # Extract the content inside \boxed{}
        return answer.lower()
    else:
        return 'No answer found'