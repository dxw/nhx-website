# Generated by Django 3.0.7 on 2020-10-20 09:52

from django.db import migrations
import modules.core.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailnhsukfrontend.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0036_auto_20201006_1029"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sectionpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("rich_text", wagtail.blocks.RichTextBlock(group=" Content")),
                    (
                        "block_quote",
                        wagtail.blocks.BlockQuoteBlock(group=" Content"),
                    ),
                    ("embed", modules.core.blocks.EmbedBlock(group=" Content")),
                    (
                        "captioned_embed",
                        wagtail.blocks.StructBlock(
                            [
                                ("embed", modules.core.blocks.EmbedBlock()),
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "sub_title",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                            ],
                            group=" Content",
                        ),
                    ),
                    (
                        "image",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "content_image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=True
                                    ),
                                ),
                                (
                                    "alt_text",
                                    wagtail.blocks.CharBlock(
                                        help_text="Only leave this blank if the image is decorative.",
                                        required=False,
                                    ),
                                ),
                                (
                                    "caption",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                            ],
                            group=" NHS Components",
                        ),
                    ),
                    (
                        "panel",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "label",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "heading_level",
                                    wagtail.blocks.IntegerBlock(
                                        default=3,
                                        help_text="The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.",
                                        max_value=4,
                                        min_value=2,
                                    ),
                                ),
                                (
                                    "body",
                                    wagtail.blocks.RichTextBlock(required=True),
                                ),
                            ],
                            group=" NHS Components",
                        ),
                    ),
                    (
                        "promo",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "link_page",
                                    wagtail.blocks.PageChooserBlock(
                                        label="Page", required=False
                                    ),
                                ),
                                (
                                    "url",
                                    wagtail.blocks.URLBlock(
                                        label="URL", required=False
                                    ),
                                ),
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(required=True),
                                ),
                                (
                                    "description",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "content_image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        label="Image", required=False
                                    ),
                                ),
                                (
                                    "alt_text",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "size",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[("", "Default"), ("small", "Small")],
                                        required=False,
                                    ),
                                ),
                                (
                                    "heading_level",
                                    wagtail.blocks.IntegerBlock(
                                        default=3,
                                        help_text="The heading level affects users with screen readers. Default=3, Min=2, Max=4.",
                                        max_value=4,
                                        min_value=2,
                                    ),
                                ),
                            ],
                            group=" NHS Components",
                        ),
                    ),
                    (
                        "expander",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(required=True)),
                                (
                                    "body",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "richtext",
                                                wagtail.blocks.RichTextBlock(),
                                            ),
                                            (
                                                "action_link",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "text",
                                                            wagtail.blocks.CharBlock(
                                                                label="Link text",
                                                                required=True,
                                                            ),
                                                        ),
                                                        (
                                                            "external_url",
                                                            wagtail.blocks.URLBlock(
                                                                label="URL",
                                                                required=True,
                                                            ),
                                                        ),
                                                        (
                                                            "new_window",
                                                            wagtail.blocks.BooleanBlock(
                                                                label="Open in new window",
                                                                required=False,
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "inset_text",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "body",
                                                            wagtail.blocks.RichTextBlock(
                                                                required=True
                                                            ),
                                                        )
                                                    ]
                                                ),
                                            ),
                                            (
                                                "image",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "content_image",
                                                            wagtail.images.blocks.ImageChooserBlock(
                                                                required=True
                                                            ),
                                                        ),
                                                        (
                                                            "alt_text",
                                                            wagtail.blocks.CharBlock(
                                                                help_text="Only leave this blank if the image is decorative.",
                                                                required=False,
                                                            ),
                                                        ),
                                                        (
                                                            "caption",
                                                            wagtail.blocks.CharBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "grey_panel",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "label",
                                                            wagtail.blocks.CharBlock(
                                                                label="heading",
                                                                required=False,
                                                            ),
                                                        ),
                                                        (
                                                            "heading_level",
                                                            wagtail.blocks.IntegerBlock(
                                                                default=3,
                                                                help_text="The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.",
                                                                max_value=4,
                                                                min_value=2,
                                                            ),
                                                        ),
                                                        (
                                                            "body",
                                                            wagtail.blocks.RichTextBlock(
                                                                required=True
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "warning_callout",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "title",
                                                            wagtail.blocks.CharBlock(
                                                                default="Important",
                                                                required=True,
                                                            ),
                                                        ),
                                                        (
                                                            "heading_level",
                                                            wagtail.blocks.IntegerBlock(
                                                                default=3,
                                                                help_text="The heading level affects users with screen readers. Default=3, Min=2, Max=4.",
                                                                max_value=4,
                                                                min_value=2,
                                                                required=True,
                                                            ),
                                                        ),
                                                        (
                                                            "body",
                                                            wagtail.blocks.RichTextBlock(
                                                                required=True
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            (
                                                "summary_list",
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "rows",
                                                            wagtail.blocks.ListBlock(
                                                                wagtailnhsukfrontend.blocks.SummaryListRowBlock
                                                            ),
                                                        ),
                                                        (
                                                            "no_border",
                                                            wagtail.blocks.BooleanBlock(
                                                                default=False,
                                                                required=False,
                                                            ),
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            ("table", modules.core.blocks.TableBlock()),
                                        ],
                                        required=True,
                                    ),
                                ),
                            ],
                            group=" NHS Components",
                        ),
                    ),
                    (
                        "grey_panel",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "label",
                                    wagtail.blocks.CharBlock(
                                        label="heading", required=False
                                    ),
                                ),
                                (
                                    "heading_level",
                                    wagtail.blocks.IntegerBlock(
                                        default=3,
                                        help_text="The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.",
                                        max_value=4,
                                        min_value=2,
                                    ),
                                ),
                                (
                                    "body",
                                    wagtail.blocks.RichTextBlock(required=True),
                                ),
                            ],
                            group=" NHS Components",
                        ),
                    ),
                    (
                        "inset_text",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "body",
                                    wagtail.blocks.RichTextBlock(required=True),
                                )
                            ],
                            group=" NHS Components",
                        ),
                    ),
                    (
                        "panel_list",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "panels",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "left_panel",
                                                    wagtail.blocks.StructBlock(
                                                        [
                                                            (
                                                                "label",
                                                                wagtail.blocks.CharBlock(
                                                                    required=False
                                                                ),
                                                            ),
                                                            (
                                                                "heading_level",
                                                                wagtail.blocks.IntegerBlock(
                                                                    default=3,
                                                                    help_text="The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.",
                                                                    max_value=4,
                                                                    min_value=2,
                                                                ),
                                                            ),
                                                            (
                                                                "body",
                                                                wagtail.blocks.RichTextBlock(
                                                                    required=True
                                                                ),
                                                            ),
                                                        ]
                                                    ),
                                                ),
                                                (
                                                    "right_panel",
                                                    wagtail.blocks.StructBlock(
                                                        [
                                                            (
                                                                "label",
                                                                wagtail.blocks.CharBlock(
                                                                    required=False
                                                                ),
                                                            ),
                                                            (
                                                                "heading_level",
                                                                wagtail.blocks.IntegerBlock(
                                                                    default=3,
                                                                    help_text="The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.",
                                                                    max_value=4,
                                                                    min_value=2,
                                                                ),
                                                            ),
                                                            (
                                                                "body",
                                                                wagtail.blocks.RichTextBlock(
                                                                    required=True
                                                                ),
                                                            ),
                                                        ]
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                )
                            ],
                            group=" NHS Components",
                        ),
                    ),
                    (
                        "promo_group",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "column",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("one-half", "One-half"),
                                            ("one-third", "One-third"),
                                        ]
                                    ),
                                ),
                                (
                                    "size",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[("", "Default"), ("small", "Small")],
                                        required=False,
                                    ),
                                ),
                                (
                                    "heading_level",
                                    wagtail.blocks.IntegerBlock(
                                        default=3,
                                        help_text="The heading level affects users with screen readers. Default=3, Min=2, Max=4.",
                                        max_value=4,
                                        min_value=2,
                                    ),
                                ),
                                (
                                    "promos",
                                    wagtail.blocks.ListBlock(
                                        modules.core.blocks.BasePromoBlock
                                    ),
                                ),
                            ],
                            group=" NHS Components",
                        ),
                    ),
                    (
                        "warning_callout",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        default="Important", required=True
                                    ),
                                ),
                                (
                                    "heading_level",
                                    wagtail.blocks.IntegerBlock(
                                        default=3,
                                        help_text="The heading level affects users with screen readers. Default=3, Min=2, Max=4.",
                                        max_value=4,
                                        min_value=2,
                                        required=True,
                                    ),
                                ),
                                (
                                    "body",
                                    wagtail.blocks.RichTextBlock(required=True),
                                ),
                            ],
                            group=" NHS Components",
                        ),
                    ),
                    ("table", modules.core.blocks.TableBlock(group=" NHS Components")),
                    (
                        "panel_table",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("table", modules.core.blocks.TableBlock()),
                            ],
                            group=" NHS Components",
                        ),
                    ),
                    (
                        "action_link",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "text",
                                    wagtail.blocks.CharBlock(
                                        label="Link text", required=True
                                    ),
                                ),
                                (
                                    "external_url",
                                    wagtail.blocks.URLBlock(
                                        label="URL", required=True
                                    ),
                                ),
                                (
                                    "new_window",
                                    wagtail.blocks.BooleanBlock(
                                        label="Open in new window", required=False
                                    ),
                                ),
                            ],
                            group=" NHS Components",
                        ),
                    ),
                    (
                        "latest_blog_posts",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(required=True),
                                ),
                                (
                                    "number_of_posts",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[(1, "One"), (2, "Two"), (3, "Three")]
                                    ),
                                ),
                                (
                                    "tag_id",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=modules.core.blocks.get_tag_list
                                    ),
                                ),
                            ],
                            group=" Content",
                        ),
                    ),
                    (
                        "latest_news",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(required=True),
                                ),
                                (
                                    "number_of_posts",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[(1, "One"), (2, "Two"), (3, "Three")]
                                    ),
                                ),
                                (
                                    "tag_id",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=modules.core.blocks.get_tag_list
                                    ),
                                ),
                            ],
                            group=" Content",
                        ),
                    ),
                    (
                        "promo_banner",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "link_page",
                                    wagtail.blocks.PageChooserBlock(
                                        label="Page", required=False
                                    ),
                                ),
                                (
                                    "url",
                                    wagtail.blocks.URLBlock(
                                        label="URL", required=False
                                    ),
                                ),
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(required=True),
                                ),
                                (
                                    "description",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "content_image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        label="Image", required=False
                                    ),
                                ),
                                (
                                    "alt_text",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "call_to_action",
                                    wagtail.blocks.CharBlock(required=True),
                                ),
                                (
                                    "heading_level",
                                    wagtail.blocks.IntegerBlock(
                                        default=3,
                                        help_text="The heading level affects users with screen readers. Default=3, Min=2, Max=4.",
                                        max_value=4,
                                        min_value=2,
                                    ),
                                ),
                                (
                                    "image_alignment",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[("right", "Right"), ("left", "Left")]
                                    ),
                                ),
                            ],
                            group=" Content",
                        ),
                    ),
                    (
                        "newsletter_signup",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(required=True),
                                ),
                                (
                                    "heading_level",
                                    wagtail.blocks.IntegerBlock(
                                        default=3,
                                        help_text="The heading level affects users with screen readers. Default=3, Min=2, Max=4.",
                                        max_value=4,
                                        min_value=2,
                                    ),
                                ),
                                (
                                    "description",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "mailing_list_id",
                                    wagtail.blocks.CharBlock(required=True),
                                ),
                            ],
                            group=" Content",
                        ),
                    ),
                    (
                        "step_group",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "heading",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "steps",
                                    wagtail.blocks.ListBlock(
                                        modules.core.blocks.StepBlock
                                    ),
                                ),
                            ],
                            group=" Content",
                        ),
                    ),
                ],
                blank=True,
                verbose_name="Body blocks",
            ),
        ),
    ]
