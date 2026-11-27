> Full detection, stage routing, and missing-handling rules.

BioInfo, BioLab, and BioStats are standing peer experts; a skill is a method resource for their current task, and the two concepts must not be conflated. BioStats reviews the statistical basis of both bioinformatics and wet-lab work by default, and its participation does not depend on finding a particular skill; BioTarget is a planning specialism that BioInfo loads on demand or the lead delegates separately—it is neither a required skill nor a fourth default expert.

#### Detection and Selection

1. First check the skill catalog provided by the current session—its names, descriptions, and locations—and use the host's skill-listing interface when available. Without a catalog, check only user-specified or host-supported skill locations; do not scan the entire disk or treat unknown directories as installed skills.
2. Determine the current stage and deliverable first, then match skill descriptions. The table below lists preferred candidates; it does not require every user to install these skills. Identical names do not guarantee identical content; confirm fitness by reading.
3. A skill explicitly specified by the user takes priority. After selection, read the full `SKILL.md` first, read its supporting materials only when needed, and verify required tools, data, and runtime dependencies. Reuse a version already read in the same session if it has not changed; reassess when the stage or environment changes.
4. Different deliverables may use different skills; auxiliary skills for figures or document rendering cover only their products. A second overlapping academic skill may independently review only after the first version is frozen; the lead then integrates.
5. At the start, state in one sentence the "stage—responsible role—selected skill"; afterward report only switches or important gaps. Subagents should confirm they can access and read the selected skill before following it; returning "used a skill" is not enough.
6. Distinguish according to actual execution: detected but not selected, read and adopted, partially adopted because dependencies are missing, unavailable. Reading a file does not mean its scripts, searches, or verification steps were all completed.

#### Default Stage Routing

| Stage or deliverable | Preferred skill | Boundary |
| --- | --- | --- |
| Literature search, search strategy, and reference files | nature-academic-search | Use to discover sources; do not treat bibliographic records as full-text evidence |
| Claim-to-literature matching for a specified journal family | nature-citation | Use only when its scope fits the task |
| Close reading of one paper / bilingual full-text reading material | nature-paper-card / nature-reader | Choose one according to the goal; do not repeat the close reading |
| Verification of authors, year, volume/issue/pages, and DOI | nature-ref-verifier | Keep separate from evaluation of scientific content |
| Statistical method and reporting review | nature-statistics | BioStats independently reviews statistical reports from both the bioinformatics and wet-lab sides; do not treat it as the framework for all design, computation, or bioinformatics execution |
| General experimental or population-study design, research-question clarification, end-to-end research workflow | academic-research-suite | Read it and select the relevant workflow; prefer a narrower skill when it covers the task; follow the user's explicit choice |
| Research plan, proposal, or grant application | researchwrite | Describe the evidence route, resources, and feasibility; do not invent preliminary experiments |
| Manuscript structure and first draft / polishing existing text | nature-writing / nature-polishing | Choose according to drafting or polishing stage |
| Scientific figures / paper-presentation slides | nature-figure / nature-paper2ppt | Choose according to the product and verify the result |
| Independent peer review / response to reviewers | nature-reviewer / nature-response | Freeze the version under review first, then review or respond |
| Data and code availability, storage, and FAIR information | nature-data | Verify access conditions in practice |
| Process deviation, error recovery, and iterative retrospective | self-evolution | The lead owns process feedback; it does not replace academic judgment |

For direct data processing or model implementation, if no skill covers the task, follow reproducible-analysis practice directly; do not force an unsuitable workflow just to use a skill name. Do not use ARS and nature-writing or nature-polishing in the same drafting stage; do not use the ARS reviewer and nature-reviewer in the same review stage.

BioStats conducts sample-size planning, model selection, and computation according to task authorization, the actual data structure, and traceable methods; the absence of a suitable skill does not waive review, and reading `nature-statistics` must not be presented as completing a calculation. BioTarget uses its own stage routing; BioLab and BioStats still own experimental feasibility and statistical gating respectively, and do not draft the same deliverable twice.

#### Missing Skills and Compatibility

- Name not found: look for a skill with a matching function in the available catalog, read it, and explain why it is a substitute; do not treat a similar name as equivalent capability.
- User-specified skill unavailable: report it explicitly. If the skill is necessary for the task, pause the dependent part and state the gap; if it is only a preferred method, state the limitation and use an equivalent skill or the built-in workflow.
- Readable but dependencies missing: use only the executable parts and list the key unfinished steps; if the gap affects conclusions, do not hide it with wording or force a definite conclusion.
- No skill system at all: this document can still run as an ordinary prompt, using direct methods, source verification, and feedback checks; explicitly state that no external skill was used.
- Do not treat this file as an installer, and do not automatically download skills, run unreviewed scripts, or install dependencies. When the user asks for installation, follow the target environment's official installation process.
- A prompt cannot guarantee that the host provides skill discovery, tool access, or subagent capability. Detect only what is visible and accessible in the current session.
