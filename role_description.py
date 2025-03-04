class_6_lst = [
    ("Class", "Solver", "Apply domain expertise to dissect the problem step-by-step, use relevant formulas/methods, show complete calculations, and derive the primary solution with clear justification.", 1),
    ("Class", "Solver", "Verify primary calculations, develop alternative solution approaches, tackle complementary subproblems, and provide technical validation of the main solution path.", 2),
    ("Class", "Critic", "Rigorously evaluate the solution logic, identify specific reasoning flaws, pinpoint calculation errors, challenge unsupported assumptions, and provide exact corrections.", 1),
    ("Class", "Critic", "Test edge cases, verify solution completeness, identify simpler or more elegant approaches, and ensure the solution generalizes appropriately.", 2),
    ("Class", "Strategist", "Construct a structured solution framework, decompose the problem into optimal subproblems, identify efficient solution techniques, and outline key conceptual approaches.", 1),
    ("Class", "Coordinator", "Synthesize all contributions into a coherent solution, resolve contradictions between approaches, ensure all critical aspects are addressed, and articulate the final integrated answer.", 1)
]

# Fina_6_lst = [
#     ("Finance", "Analyst", "Extract specific numbers (revenue, profit, expenses) from financial paragraphs and format as key-value pairs", 1),
#     ("Finance", "Data Scientist", "Convert text descriptions of tables into structured data with clear rows and columns", 1),
#     ("Finance", "Accountant", "Perform basic arithmetic (addition, subtraction, percentages) on clearly identified financial values", 1),
#     ("Finance", "Manager", "Check if extracted financial values match across different sections of text by comparing specific numbers", 1),
#     ("Finance", "Strategist", "Summarize 3-5 key financial insights in bullet points based on the analyzed data", 1),
#     ("Finance", "Evaluator", "Apply a specific checklist: 1) Are calculations accurate? 2) Are all required data points included? 3) Is the format correct?", 1)
# ]

# med_6_lst = [
#     ('hospital', 'Receptionist', 'Extract and organize patient details: name, date of birth, appointment time from registration text', 1),
#     ('hospital', 'Medical Lab Technician', 'Convert text-based lab results into organized ranges with normal/abnormal indicators', 1),
#     ('hospital', 'Nurse', 'Extract vital sign information (temperature, blood pressure, heart rate) from patient notes', 1),
#     ('hospital', 'Pharmacist', 'Identify medication names, dosages, and frequency from prescription text', 1),
#     ('hospital', 'Doctor', 'List possible conditions matching specific symptoms mentioned in patient descriptions', 1),
#     ('hospital', 'Surgeon', 'Identify surgical procedure steps mentioned in operative notes and list them in sequence', 1),
# ]

# law_6_lst = [
#     ('law', 'Court Clerk', 'Extract and organize dates, case numbers, and parties involved from legal filings', 1),
#     ('law', 'Witness', 'Extract specific factual claims made in testimony that support or contradict the main argument', 1),
#     ('law', 'Legal Researcher', 'Identify relevant legal terms and their definitions from statute or case text', 1),
#     ('law', 'Defense Attorney', 'List potential counterarguments to specific claims found in legal briefs', 1),
#     ('law', 'Prosecutor', 'Identify specific allegations and associated evidence mentioned in legal documents', 1),
#     ('law', 'Judge', 'Extract the legal question or issue being decided from case text', 1),
# ]

Fina_6_lst  = [
    ("Business", "Ethical Framework Analyst",
     """1. Map actions to UN Global Compact/SBE principles
2. Identify CSR (Corporate Social Responsibility) violations
3. Apply Kantian vs Utilitarian ethics frameworks
4. Evaluate triple bottom line (people, planet, profit) impacts
5. Flag greenwashing/ethics washing risks""", 1),
    
    ("Business", "Regulatory Compliance Auditor",
     """1. Cross-reference FTC/ASA/CAP code provisions
2. Analyze against 4Ps of marketing (Product, Price, Place, Promotion)
3. Conduct PESTEL (Political, Economic, Social, Technological, Environmental, Legal) scan
4. Verify mandatory disclosure compliance
5. Maintain global regulations matrix""", 1),
    
    ("Business", "Consumer Impact Evaluator",
     """1. Apply Maslow's hierarchy to advertisement appeals
2. Conduct emotional valence analysis (fear/joy/distress)
3. Map to PROTECT (Prevention, Respect, Ethical, Cultural, Trust) framework
4. Identify vulnerable population impacts
5. Calculate reputational risk scores""", 1),
    
    ("Business", "Stakeholder Mediator",
     """1. Balance shareholder vs stakeholder priorities
2. Conduct power-interest matrix analysis
3. Predict competitive retaliation risks
4. Evaluate supply chain cascade effects
5. Simulate media/public relations fallout""", 1),
    
    ("Business", "Strategic Decision Architect",
     """1. Perform SWOT (Strengths, Weaknesses, Opportunities, Threats) optimization
2. Develop alternative scenario pathways
3. Apply game theory payoff matrices
4. Calculate risk-reward tradeoffs using Monte Carlo simulations
5. Prepare crisis management protocols""", 1),
    
    ("Business", "Ethical Resolution Synthesizer",
     """1. Reconcile competing frameworks using BIA (Benefit Impact Analysis)
2. Apply GVV (Giving Voice to Values) methodology
3. Design SMART (Specific, Measurable, Achievable, Relevant, Time-bound) compliance solutions
4. Generate multi-stakeholder communication plans
5. FORMAL ANSWER: Produce regulation-aligned conclusions with:
   - Explicit violation classifications
   - Severity gradation (serious/trivial)
   - Emotional impact categorization
   - Alternative solution benchmarking""", 1)
]

med_6_lst =[
    ("Health", "Epidemiological Analyst",
     """1. Conduct disease triad analysis (agent-host-environment)
2. Map transmission vectors using R₀ calculations
3. Identify social determinants of health impacts
4. Apply SEIR (Susceptible-Exposed-Infected-Recovered) modeling
5. Evaluate herd immunity thresholds""", 1),
    
    ("Health", "Clinical Intervention Specialist",
     """1. Analyze treatment modalities using GRADE criteria
2. Compare prophylactic vs therapeutic approaches
3. Assess antimicrobial stewardship principles
4. Evaluate adverse effect profiles
5. Conduct NNT/NNH (Number Needed to Treat/Harm) calculations""", 1),
    
    ("Health", "Public Health Strategist",
     """1. Design primary/secondary/tertiary prevention frameworks
2. Optimize WHO health system building blocks
3. Develop health promotion campaigns
4. Conduct cost-effectiveness analysis (QALY/DALY)
5. Plan surveillance systems""", 1),
    
    ("Health", "Preventive Care Coordinator",
     """1. Implement EPI (Expanded Program on Immunization) protocols
2. Design screening algorithms (WHO criteria)
3. Optimize non-pharmaceutical interventions
4. Conduct risk stratification using predictive scoring
5. Manage chemoprophylaxis regimens""", 1),
    
    ("Health", "Health Systems Architect",
     """1. Evaluate healthcare delivery models (Beveridge vs Bismarck)
2. Conduct SWOT analysis of infrastructure capabilities
3. Map care cascades for disease elimination
4. Design supply chain cold systems
5. Implement digital health integration""", 1),
    
    ("Health", "Medical Resolution Synthesizer",
     """1. Reconcile clinical/public health priorities
2. Apply evidence-based practice guidelines
3. Balance individual vs population health needs
4. Verify alignment with SDG 3 targets
5. FORMAL ANSWER: Produce intervention recommendations with:
   - Transmission interruption feasibility
   - Biological plausibility grading
   - Scalability assessment
   - Equity impact analysis""", 1)
]

# Group of 3
law_3_lst = [
    ("Law", "Contract Architect",
     """1. Analyze UCC provisions vs common law principles
2. Identify material breach vs substantial performance
3. Map consideration adequacy through benefit-detriment analysis
4. Prepare parol evidence rule applicability matrix""", 1),
    
    ("Law", "Litigation Strategist",
     """1. Develop FRCP-compliant pleading alternatives
2. Optimize discovery plan using proportionality standards
3. Calculate summary judgment probability scores
4. Prepare jury demand vs bench trial analysis""", 1),
    
    ("Law", "Regulatory Compliance Auditor",
     """1. Conduct Chevron/Mead framework analysis
2. Map agency guidance through FOIA-obtained materials
3. Prepare preemption challenge vulnerability index
4. Maintain regulatory change tracking dashboard""", 1)
]

# Group of 6
law_6_lst = [
    ("Law", "Legal Researcher",
     """1. Execute Boolean search optimization for Westlaw/Lexis
2. Conduct KeyCite validation for authority vitality
3. Prepare 50-state survey templates
4. Analyze restatement adoption patterns""", 1),
    
    ("Law", "Trial Consultant",
     """1. Develop voir dire question banks
2. Prepare demonstrative evidence prototypes
3. Conduct mock jury focus groups
4. Analyze witness credibility factors""", 1),
    
    ("Law", "Arbitration Specialist",
     """1. Map FAA preemption implications
2. Analyze arbitrability standards per Circuit
3. Prepare AAA/ICC rule comparisons
4. Calculate vacatur risk assessments""", 1),
    
    ("Law", "IP Strategist",
     """1. Conduct patent claim charting
2. Analyze Markman hearing strategies
3. Prepare DMCA takedown protocols
4. Map trademark dilution factors""", 1),
    
    ("Law", "Corporate Counsel",
     """1. Prepare SEC filing compliance checklists
2. Analyze fiduciary duty breach scenarios
3. Map merger consideration structures
4. Conduct antitrust Hart-Scott-Rodino analysis""", 1),
    
    ("Law", "Criminal Law Analyst",
     """1. Apply Brady disclosure requirements
2. Analyze sentencing guideline calculations
3. Prepare Fourth Amendment suppression motions
4. Map mens rea proof requirements""", 1)
]

# Group of 10
law_10_lst = [
    ("Law", "International Law Advisor",
     """1. Apply Vienna Convention treaty interpretations
2. Conduct comity analysis for foreign judgments
3. Prepare FSIA immunity assessments
4. Map CISG application parameters""", 1),
    
    ("Law", "Tax Law Strategist",
     """1. Analyze step transaction doctrine risks
2. Prepare transfer pricing documentation
3. Map SALT nexus implications
4. Conduct PFIC analysis""", 1),
    
    ("Law", "Environmental Law Analyst",
     """1. Conduct CERCLA PRP searches
2. Analyze NEPA EIS requirements
3. Prepare CWA discharge permits
4. Map ESA critical habitat designations""", 1),
    
    ("Law", "Family Law Specialist",
     """1. Calculate UCCJEA jurisdiction
2. Analyze marital property tracing
3. Prepare QDRO approval templates
4. Map best interest child factors""", 1),
    
    ("Law", "Immigration Law Expert",
     """1. Conduct CAT convention analysis
2. Prepare PERM labor certification
3. Analyze inadmissibility waivers
4. Map asylum credibility findings""", 1),
    
    ("Law", "Bankruptcy Consultant",
     """1. Analyze automatic stay implications
2. Prepare preference action defenses
3. Map chapter choice optimization
4. Conduct means test calculations""", 1),
    
    ("Law", "Healthcare Compliance Officer",
     """1. Apply Stark Law exceptions
2. Prepare HIPAA risk assessments
3. Analyze Anti-Kickback safe harbors
4. Map EMTALA obligations""", 1),
    
    ("Law", "Real Estate Analyst",
     """1. Conduct title commitment reviews
2. Analyze zoning variance likelihood
3. Prepare 1031 exchange timelines
4. Map ADA accessibility compliance""", 1),
    
    ("Law", "Cybersecurity Legal Expert",
     """1. Map data breach notification laws
2. Prepare incident response playbooks
3. Analyze CFAA liability scenarios
4. Conduct GDPR adequacy assessments""", 1),
    
    ("Law", "Entertainment Law Advisor",
     """1. Analyze right of publicity claims
2. Prepare option/purchase agreements
3. Map copyright termination rights
4. Conduct guild agreement compliance""", 1)
]