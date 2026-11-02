"""Build Mohammad Madadi's CV PDF. Not part of the website."""

from pathlib import Path

from fpdf import FPDF

FONT = Path(r"C:\Windows\Fonts")
OUTS = [
    Path(r"D:\Mohammad\Github\MoeMadadi.github.io\cv\Mohammad_Madadi_CV.pdf"),
    Path(r"D:\Mohammad\Github\MoeMadadi.github.io\assets\pdf\cv.pdf"),
    Path(r"D:\Mohammad\Github\MoeMadadi.github.io\assets\pdf\Mohammad_Madadi_CV.pdf"),
    Path("D:/Mohammad/APPLY") / "تلاش آخر قبل از خودکشی" / "Mohammad_Madadi_CV.pdf",
]


class CV(FPDF):
    def __init__(self):
        super().__init__(format="Letter", unit="mm")
        self.add_font("Calibri", "", str(FONT / "calibri.ttf"))
        self.add_font("Calibri", "B", str(FONT / "calibrib.ttf"))
        self.add_font("Calibri", "I", str(FONT / "calibrii.ttf"))
        self.add_font("Calibri", "BI", str(FONT / "calibriz.ttf"))
        self.set_auto_page_break(auto=True, margin=12)
        self.set_margins(14, 12, 14)

    def section(self, title):
        self.ln(1.6)
        self.set_font("Calibri", "B", 11)
        self.set_text_color(15, 45, 90)
        self.cell(0, 5.2, title.upper(), new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(15, 45, 90)
        y = self.get_y()
        self.line(self.l_margin, y, self.w - self.r_margin, y)
        self.ln(1.4)
        self.set_text_color(0, 0, 0)

    def role(self, left, right):
        self.set_font("Calibri", "B", 10.5)
        self.cell(self.epw * 0.72, 4.6, left)
        self.set_font("Calibri", "", 10.5)
        self.cell(self.epw * 0.28, 4.6, right, align="R", new_x="LMARGIN", new_y="NEXT")

    def sub(self, text):
        self.set_font("Calibri", "I", 10)
        self.multi_cell(0, 4.4, text)
        self.ln(0.3)

    def bullet(self, text):
        self.set_font("Calibri", "", 10)
        self.set_x(self.l_margin)
        self.cell(4, 4.3, "-")
        self.multi_cell(self.epw - 4, 4.3, text)


def build():
    pdf = CV()
    pdf.add_page()
    pdf.set_font("Calibri", "B", 18)
    pdf.cell(0, 8, "Mohammad Madadi", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Calibri", "", 10)
    pdf.cell(
        0,
        4.6,
        "mohammadmadadi2001@gmail.com  |  moemadadi.github.io  |  +98 993 007 4297",
        align="C",
        new_x="LMARGIN",
        new_y="NEXT",
    )
    pdf.cell(
        0,
        4.6,
        "linkedin.com/in/MoeMadadi  |  github.com/MoeMadadi",
        align="C",
        new_x="LMARGIN",
        new_y="NEXT",
    )

    pdf.section("Research interests")
    pdf.set_font("Calibri", "", 10)
    pdf.multi_cell(
        0,
        4.4,
        "Robotics and autonomous systems; embodied AI; continual learning; robot learning; reinforcement learning; motion planning.",
    )

    pdf.section("Education")
    pdf.role("Sharif University of Technology", "Tehran, Iran")
    pdf.sub("B.Sc. in Mechanical Engineering; GPA: 17.66/20.    Sep 2019 - Jul 2024")
    pdf.bullet(
        "Ranked 9th in the Robotics and Control division and 24th overall among 147 Mechanical Engineering students."
    )

    pdf.section("Research experience")
    pdf.role("University of Hong Kong", "Hong Kong")
    pdf.sub(
        "Research Assistant (Remote), Agentic Intelligence Lab - Advisor: Prof. Jiayu Chen.    Sep 2025 - Present"
    )
    for item in [
        "Task-free online continual learning: developed Streaming Subspace Routing (SSR), which uses frozen, unprompted ViT-B/16 feature geometry to route inputs among low-rank LoRA experts without task identity or class-based routing at inference.",
        "Designed streaming subspace updates and soft expert composition using residual distances; applied rank-8 LoRA experts to attention query and value projections while keeping the backbone frozen.",
        "Evaluated CIFAR-100, Tiny-ImageNet, and ImageNet-R under the Si-Blurry protocol with replay budgets of 0, 500, and 2,000 samples; conducted multi-seed experiments and reported Aauc, Alast, and Flast.",
        "Built a preceding shared-prompt method with slow-learning LoRA adapters and EMA-based logit distillation. Across 500- and 2,000-sample replay settings, it improved over SinglePrompt on all three datasets; ImageNet-R gains reached +6.62 Aauc and +7.19 Alast.",
        "Continual robot learning: conducted preliminary research on BEHAVIOR-1K household-manipulation tasks using OmniGibson and Isaac Sim, including task-stream design and demonstration-based learning considerations.",
        "Continual diffusion policies: investigated sequential adaptation across the Lift, Can, and Square manipulation tasks in Robomimic, focusing on specialization, forward transfer, and knowledge distillation between task stages.",
    ]:
        pdf.bullet(item)

    pdf.role("Sharif University of Technology", "Tehran, Iran")
    pdf.sub(
        "Research Assistant, Department of Mechanical Engineering - Advisor: Prof. Mohammad Taghi Ahmadian.    Jul 2024 - Dec 2024"
    )
    pdf.bullet(
        "Implemented, trained, and compared PPO, TD3, and SAC for Franka Panda assistive-arm motion planning in simulation."
    )
    pdf.bullet(
        "Performed Optuna hyperparameter tuning, compared convergence under manual and optimized settings, analyzed results, prepared figures, and contributed to the conference manuscript."
    )

    pdf.role("Sharif University of Technology", "Tehran, Iran")
    pdf.sub(
        "Research Assistant, Spine Biomechanics Laboratory - Advisor: Prof. Navid Arjmand.    Sep 2022 - Jul 2023"
    )
    pdf.bullet(
        "Independently collected workplace posture data, developed biomechanical models in 3DSSPP and AnyBody, and quantified ergonomic and spinal-injury risks for B.Sc. thesis research."
    )
    pdf.bullet(
        "Designed and evaluated a workstation-tilter intervention that reduced model-estimated ergonomic risk by more than 50% and lowered estimated L4-L5 compression force."
    )

    pdf.role("Research Center of Intelligent Neuro-Rehabilitation", "Tehran, Iran")
    pdf.sub("Research Assistant - Advisor: Prof. Navid Arjmand.    Sep 2022 - Feb 2023")
    pdf.bullet(
        "Collected in vivo kinematic and force data for gait and manual material handling studies using laboratory motion-analysis and force-measurement equipment."
    )

    pdf.section("Publications and manuscripts")
    pdf.bullet(
        'Madadi, M. "Learning directional locomotion under actuator rate loss in a triangular microswimmer." Manuscript in preparation for Robotics and Autonomous Systems.'
    )
    pdf.bullet(
        'Naeimi Tabiei, P., Haji Zargarbashi, M., Madadi, M., and Ahmadian, M. T. "The Role of Deep Reinforcement Learning in Motion Planning for Robotic Arm Assistive Systems." 33rd Annual International Conference of the Iranian Society of Mechanical Engineers, Tehran, 2025. Civilica: ISME33_085.'
    )

    pdf.section("Selected projects")
    pdf.bullet(
        "Triangular microswimmer - learned directional locomotion under actuator rate loss. Manuscript in preparation for Robotics and Autonomous Systems. Code: github.com/MoeMadadi/triangular-microswimmer-rl"
    )
    pdf.bullet("Counterfactual safety learning - early-stage project.")
    pdf.bullet(
        "Maze solving with Markov decision processes - formulated maze navigation as an MDP and implemented reinforcement-learning algorithms for policy learning and path selection. Code: github.com/MoeMadadi/Maze-Solver-using-Markov-Decision-Processes"
    )
    pdf.bullet(
        "Snakefield - a Snake game with Minesweeper-style mechanics, written in C with raylib. Code: github.com/MoeMadadi/Snakefield"
    )

    pdf.section("Teaching experience")
    pdf.role("Sharif University of Technology", "Tehran, Iran")
    pdf.bullet("Teaching Assistant, Machine Dynamics - Prof. Saeed Behzadipor.")
    pdf.bullet("Teaching Assistant, Mechanical Engineering Graphics - Prof. Hamid Haghshenas.")

    pdf.section("Honors and awards")
    pdf.bullet("First Class Honours, B.Sc. in Mechanical Engineering, Sharif University of Technology (2024).")
    pdf.bullet(
        "Ranked 9th among approximately 164,000 participants in Iran's National University Entrance Examination (2019)."
    )

    pdf.section("Technical skills and languages")
    pdf.set_font("Calibri", "", 10)
    lines = [
        "Programming: Python, C, MATLAB/Simulink, Arduino",
        "Machine learning: PyTorch, continual learning, reinforcement learning, LoRA, knowledge distillation",
        "Robotics and simulation: Isaac Sim, OmniGibson, Robomimic",
        "Experimentation: multi-seed evaluation, ablation studies, hyperparameter optimization, Optuna",
        "Development tools: Git, Linux, LaTeX",
        "Engineering: ANSYS Fluent, SOLIDWORKS, 3DSSPP, Jack, Vicon Nexus, AnyBody",
        "Languages: Persian (native), English (TOEFL iBT 108/120)",
    ]
    for line in lines:
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(pdf.epw, 4.3, line)

    data = pdf.output()
    for path in OUTS:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        print(path, path.stat().st_size)


if __name__ == "__main__":
    build()
