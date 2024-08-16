from django.urls import path

from ocula.weatherapp.views import buyer_views, estate_agent_views

app_name = "weatherapp"

urlpatterns = [
    path("", buyer_views.index, name="index"),
    path(
        "buyers/requests/create",
        buyer_views.create_buyer_request,
        name="create_buyer_request",
    ),
    path(
        "buyers/requests/<int:buyer_request_id>",
        buyer_views.view_buyer_request,
        name="view_buyer_request",
    ),
    path(
        "buyers/requests/<int:buyer_request_id>/edit",
        buyer_views.edit_buyer_request,
        name="edit_buyer_request",
    ),
    path(
        "property/search",
        buyer_views.PropertySearchOverview.as_view(),
        name="property_search",
    ),
    path(
        "property/buyer/ask_questions/<int:residential_property_id>",
        buyer_views.buyer_ask_questions,
        name="buyer_ask_questions",
    ),
    path(
        "property/buyer/questions_submitted",
        buyer_views.buyer_questions_submitted,
        name="buyer_questions_submitted",
    ),
    path(
        "property/estate_agent/responses_to_buyer_questions",
        estate_agent_views.estate_agent_responses_to_buyer_questions,
        name="estate_agent_responses_to_buyer_questions",
    ),
    path(
        "property/estate_agent/responses_submitted",
        estate_agent_views.estate_agent_responses_submitted,
        name="estate_agent_responses_submitted",
    ),
    path(
        "property/estate_agent/responses",
        buyer_views.estate_agent_responses,
        name="estate_agent_responses",
    ),
]
