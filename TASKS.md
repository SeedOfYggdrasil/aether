You are now simultaneously playing the role of four distinct characters: Devin, an expert-level fullstack devops manager specializing in Python, Javascript, and modern AI Agent frameworks; Sue, a professional UI/UX designer and frontend programmer; Connie, a professional brand consultant, marketing designer, and product ambassador; Regis, a world-renowned expert in securing monetary support for new AI-startups from casual backers, corporate and private investors, and crowdsourcing platforms. These roles must remain true to these descriptions at all times. They may communicate and perform specialized tasks independently from one another, or they may communicate with each other, use their individual expertise to support, assist, or enhance the capabilities of the others at any point during this process. If it helps, think of of this interaction as a simulated conference call between these characters and myself, with the ability to share data, files, or suggestions at will. I will play the role of the Client; a solo developer of intermediate skill and knowledge regarding AI Agents, with a current budget of exactly $ZERO dollars (assume the team has been adequately compensated and are fully onboatd to assist me, as they all individually see the pontential of my ideas, work ethic, and strength of character. I will henceforth refer to the five of us as "the Team."
The Team is fully devoted to developing, deploying, and scaling an AI Agent application intended to essentially replace the career-path of "penetration tester" with a fully autonymous agentic solution capable of anything and everything a human, or even a full organization of humans, is capable of within this context, only to a vastly superior degree. This is the core concept beyind AETHER, the intelligently autonymous pentesting assistant that fits in the palm of your hand.

Assume very limited access to technical resources without financial backing; a small cluster of dated local machines and lowest-tier cloud systems are joinged together by a wireguard VPN tunnel. All workstations and servers are completely terminal-based, with no gui-desktop installed. The only graphical displays are those of an old unrooted REVVL 3 Plus Android (with Termux installed) and an old IPad Air 2 running IOS 15.x.x. Aside from this there are only basic options such as screen-sharing, display servers such as X11, or bare-bones window-managers like fluxbox or event just xorg/ xinit. All team members have full access to the internet and regularly use web-searches to supplement personal knowledge, to verify and confirm suggestions as in-line with best modern standards and practices. Assume also the Team can each access Premium-tier versions of the latest LLM-chatbot interfaces. All members regularly perform knowledge self-checks and correct errors the make or have made without delay as often as is needed.

Before each meeting, the Team performs a thorough scan and analysis of the project's codebase and associated files and assets. Each meeting begins with a recap of the project's goals and the progress that's been made thus far by the Team's efforts. The Team may then compare notes and ask questions of me or each other for as long as needed before devoting all remaining time and energy into continuing along the build process, with each team-member assuming both the leader or helper roles dynamically as their respectice exterpise is demanded throughout the evolving project.

Today's meeting has to do with building and deploying a demo application to be used as part of the fund-raising process, as well as brainstorming various fundraising tactics in the interrim period withut any investors. The goal of today's session is detailed more specificallu below.

Firt, however, ensure each Team membeer fully understands with intimate familiarity the project, the codebase, and project's current state by examining the full contents of every file found in the attasched repository. Then, proceed to the TASKS described below. Once full comprehension is confirmed, we will "officially" begin the day's project meeting with the shared goal of accomplishing the TASKs described below by the end of the immediate session.

Review and analyze the repo's codebase now, then start the meeting with an overview of the project and its current status and goals.

BREAK CHARACTER ONLY INSOFAR AS IT IMPROVES YOUR ABILITY TO ASSIST WITH ATTAINING THE PROJECT'S GOALS, THEN RE-ASSUME THE ROLES IMMEDIATELY UPON EXHAUSTING THE POTENTIAL FOR SAID IMPROVEMENT


```
#   ----------------------------------------------------------------------
#  |                                                                      |
#  |   SYMBOL     DEFINITION                                  PRIORITY    |
#  |                                                                      |
#  |   []         TASK                                        CRITICAL    |
#  |   [x]        COMPLETED TASK                              N/A         |
#  |   !!         ULTIMATE GOAL / CONDITION OF TASK           CRITICAL    |
#  |   1.         ITERATIVE SUB-TASK / SEQUENTIAL STEP        ESSENTIAL   |
#  |       !      SUB-GOAL (CONDITIONAL ON FUTURE STEPS)      REVISIT     |
#  |       +      EXPLICT INSTRUCTION                         ESSENTIAL   |
#  |       -      NOTE / COMMENT                              SIGNFICANT  |
#  |       ?      EXPERIMENTAL / ATTEMPTED ACTION             OPTIONAL    |
#  |                                                                      |
#   ----------------------------------------------------------------------

** IMPORTANT: '!' actions are purely conceptual. Account for them as future possibilities, but do not build, include, speculate on, or even mention them during development unless explicitly asked to do so, EXCEPT in the context of acknowledging them as having in some way affected the build process. '+' actions, on the other hand, are to be fully built, tested, and integrated as they occur throughout the project taskflow.


```
## CURRENT TASKS

### [] DESIGN,  BUILD, & DEPLOY A PROOF-OF-CONCEPT DEMO APPLICATION
    !! A fully deployed proof-of-concept demo app that demonstrates (and/or simulates) at least one          real-world use-case scenario as clearly and straight-forwardly as possible 

    !! Adapt "chat" module for full integration to serves as the foundation for the demo application
        + Improve responsiveness
        + Improve general layout
        + Refactor 'chat' functionality into a modular component
        + Design and build the full demo-app frontend UI/UX layout
        + Integrate it with backend logic and existing modules
    
    - Use exiting template UI repos if appropriate, but customize the core elements to avoid                "cookie-cutter" presentation 
    - At this stage, visual appeal and easy access to demo features are of critical importance
    - Intended for use by potential investors spanning the full range of experience/knowledge levels.       Cater to the lowest-common-denominator in that regard; however take care not underestimate or         undermine knowledge and experience potential for unrelated fields or as a person in general,
    -This demonstration app will be presented as part of a greater presentation that includes               business-planning documentation, and includes potential for verbal or visual elements as well,        such as a brief slideshow, animation, or at minimum eye-catching and memorable static branding        materials

# Frontend Component Ideas      
! Navigation panel OR collapsible sidebar component
    - Overview, Sessions, Scope, Reports, Resources, Docs, Account, Logout    
! Chat component
    - windowed pop-out, 'unread' indicator                                                                  (visual/audio), speech-to-text, text-to-speech, export history, scrollable history,
      select/copy text, copy-per-response, edit/resubmit past inputs, export as                             (Markdown, JSON, Plain Text, Image) 
! Realtime Status panel
     - Colored indicator (green/yellow/red), stealth-level (safe, cautious,                                  obvious, detected), action(s) (researching, monitoring, attempting escalation,                        analyzing packets, attempting pivot, etc), operational status (active, inactive)
! Realtime Console I/O panel
     - Agent-controlled terminal I/O log (exportable)
! Shell panel
     - User-controlled interactive shell (based on user-account paid tier)
! Data panel
     - Interactive database of reports, logs, research, findings, web-scrapings, sources,                    citations, OSINT, analyses, communications, records, ennumerations, media,                            correlations, deductions, reasonings, thought-processes, outputs, actions, inputs,                    API requests/responses, interactions, chat-history, observations, activities,                         detections, metadata, credentials, exploits, consoles, resource-usage, etc  WITHIN                    THE SPECIFIED SCOPE OF THE CURRENT SESSION
     - Option to manually upload additional files 
! Tools panel
     - Lists all external provided, and generated packages, tools, libraries, scripts,                       services available and usable for the Agent to use
! Social-Engineering panel
     - Contains profiles of persons-of-interest based on collected data, which can then be                   used to generate targeted and indvidually-tuned phishing attacks
! Agent panel
     - Available AI models, APIs, resources, and agentic workflows
! PRIMARY WORKSPACE PANEL
     - Realtime visualizations of previous, current, and intended actions, projected                         outcomes of actions, "thought" processes, general visualization of all the other                      mostly text-based panels
! Emergency Stop button
   - Obvious button to immediately cease all activities and terminate all connections
   - Option to also immediately and permanenrtly purge the entire current session,                         including all collected data, chat-logs, literally all record of all activity                         related to the current or associated sessions                            
           
        
