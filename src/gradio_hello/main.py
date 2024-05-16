import gradio as gr


def main():
    def greet(name, intensity):
        return "Hello, " + name + "!" * int(intensity)

    demo = gr.Interface(
        fn=greet,
        inputs=["text", "slider"],
        outputs=["text"],
    )

    demo.launch()
    # demo.launch(server_port=8080)


if __name__ == "__main__":
    main()
