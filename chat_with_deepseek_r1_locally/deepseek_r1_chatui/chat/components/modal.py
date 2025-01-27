import reflex as rx
from chat.state import State

def modal() -> rx.Component:
    """A modal to create a new chat."""
    return rx.cond(
        State.modal_open,
        rx.box(
            # Modal overlay (background)
            rx.box(
                position="fixed",
                top="0",
                left="0",
                right="0",
                bottom="0",
                background_color="rgba(0, 0, 0, 0.6)",
                z_index="1000",
            ),
            # Modal content
            rx.vstack(
                # Modal header
                rx.hstack(
                    rx.text("Create new chat", font_size="lg", color="white"),
                    rx.button(
                        "✕",
                        on_click=State.toggle_modal,
                        color="rgba(255, 255, 255, 0.8)",
                        background_color="transparent",
                        _hover={"color": "white"},
                        cursor="pointer",
                        padding="0",
                    ),
                    justify_content="space-between",
                    align_items="center",
                    width="100%",
                    padding_x="4",
                    padding_y="3",
                ),
                # Modal body
                rx.box(
                    rx.input(
                        placeholder="Type something...",
                        on_blur=State.set_new_chat_name,
                        background_color="#222",
                        border_color="rgba(255, 255, 255, 0.2)",
                        color="white",
                        _placeholder={"color": "rgba(255, 255, 255, 0.7)"},
                        padding="2",
                        width="100%",
                        border_radius="md",
                    ),
                    width="100%",
                    padding_x="4",
                    padding_y="2",
                ),
                # Modal footer
                rx.box(
                    rx.button(
                        "Create",
                        background_color="#5535d4",
                        color="white",
                        padding_x="4",
                        padding_y="2",
                        border_radius="md",
                        _hover={"background_color": "#4c2db3"},
                        on_click=State.create_chat,
                    ),
                    width="100%",
                    padding="4",
                    display="flex",
                    justify_content="flex-end",
                ),
                position="fixed",
                top="50%",
                left="50%",
                transform="translate(-50%, -50%)",
                width="90%",
                max_width="400px",
                background_color="#222",
                border_radius="md",
                z_index="1001",
                spacing="0",
            ),
            width="100vw",
            height="100vh",
            position="fixed",
            top="0",
            left="0",
            z_index="1000",
        ),
    )


# import reflex as rx
# import reflex_chakra as rc

# from chat.state import State


# def modal() -> rx.Component:
#     """A modal to create a new chat."""
#     return rc.modal(
#         rc.modal_overlay(
#             rc.modal_content(
#                 rc.modal_header(
#                     rc.hstack(
#                         rc.text("Create new chat"),
#                         rc.icon(
#                             tag="close",
#                             font_size="sm",
#                             on_click=State.toggle_modal,
#                             color="#fff8",
#                             _hover={"color": "#fff"},
#                             cursor="pointer",
#                         ),
#                         align_items="center",
#                         justify_content="space-between",
#                     )
#                 ),
#                 rc.modal_body(
#                     rc.input(
#                         placeholder="Type something...",
#                         on_blur=State.set_new_chat_name,
#                         bg="#222",
#                         border_color="#fff3",
#                         _placeholder={"color": "#fffa"},
#                     ),
#                 ),
#                 rc.modal_footer(
#                     rc.button(
#                         "Create",
#                         bg="#5535d4",
#                         box_shadow="md",
#                         px="4",
#                         py="2",
#                         h="auto",
#                         _hover={"bg": "#4c2db3"},
#                         on_click=State.create_chat,
#                     ),
#                 ),
#                 bg="#222",
#                 color="#fff",
#             ),
#         ),
#         is_open=State.modal_open,
#     )
