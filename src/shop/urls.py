from django.urls import include
from django.urls import path

from .views import (
    BankTransferView,
    CoinifyCallbackView,
    CoinifyRedirectView,
    CoinifyThanksView,
    CreditNoteListView,
    DownloadCreditNoteView,
    DownloadInvoiceView,
    OrderDetailView,
    OrderListView,
    OrderMarkAsPaidView,
    OrderReviewAndPayView,
    PayInPersonView,
    ProductDetailView,
    QuickPayCallbackView,
    QuickPayLinkView,
    QuickPayThanksView,
    ShopIndexView,
)

app_name = "shop"

urlpatterns = [
    path("", ShopIndexView.as_view(), name="index"),
    path("products/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
    path("orders/", OrderListView.as_view(), name="order_list"),
    path(
        "orders/<int:pk>/",
        include(
            [
                path("", OrderDetailView.as_view(), name="order_detail"),
                path(
                    "review/",
                    OrderReviewAndPayView.as_view(),
                    name="order_review_and_pay",
                ),
                path(
                    "invoice/",
                    DownloadInvoiceView.as_view(),
                    name="download_invoice",
                ),
                path(
                    "mark_as_paid/",
                    OrderMarkAsPaidView.as_view(),
                    name="mark_order_as_paid",
                ),
                path(
                    "pay/creditcard/",
                    include(
                        [
                            path("", QuickPayLinkView.as_view(), name="quickpay_link"),
                            path(
                                "callback/",
                                QuickPayCallbackView.as_view(),
                                name="quickpay_callback",
                            ),
                            path(
                                "thanks/",
                                QuickPayThanksView.as_view(),
                                name="quickpay_thanks",
                            ),
                        ],
                    ),
                ),
                path(
                    "pay/blockchain/",
                    CoinifyRedirectView.as_view(),
                    name="coinify_pay",
                ),
                path(
                    "pay/blockchain/callback/",
                    CoinifyCallbackView.as_view(),
                    name="coinify_callback",
                ),
                path(
                    "pay/blockchain/thanks/",
                    CoinifyThanksView.as_view(),
                    name="coinify_thanks",
                ),
                path(
                    "pay/banktransfer/",
                    BankTransferView.as_view(),
                    name="bank_transfer",
                ),
                path("pay/in_person/", PayInPersonView.as_view(), name="in_person"),
            ],
        ),
    ),
    path("creditnotes/", CreditNoteListView.as_view(), name="creditnote_list"),
    path(
        "creditnotes/<int:pk>/pdf/",
        DownloadCreditNoteView.as_view(),
        name="download_creditnote",
    ),
]
