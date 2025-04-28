# AETHER

Refer to README.md for a higher-level technical overview

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

```
## TASKS

### [] 1. PROOF-OF-CONCEPT
    !! Deploy proof-of-concept app to demonstrate (and/or simulate) planned functionality

    1. Convert 'ai-chat<gemini>' into 'chat' submodule
        - Pre-built standalone Gemini API UI client
        + Improve responsiveness
        + Improve general layout
        + Convert to windowed modal component OR collapsible panel component
        + Refactor for modular integration
    2. Build skeleton of full UI/UX
        - Dashboard layout facillitating user-oversight of agent workflow
        + Section out into spaces to accomodate the following future components:
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
                ? Option to also immediately and permanenrtly purge the entire current session,                         including all collected data, chat-logs, literally all record of all activity                         related to the current or associated sessions                            
            
            - IMPORTANT: the above components are purely conceptual, and are the result of a                        spontaneous brainstorm of ideas for the final UI/UX. A time will come to                              further analyze and refine this section, but that time is not now. Let this section                   serve rather to vaguely and generally define one of many visions for an as-of-yet                     ephemeral production-ready build.

        
