from __future__ import annotations

import os
from typing import Any, List, Optional, Union

from pydantic import BaseModel, Field



class GaListData(BaseModel):
    item_list_id: str
    item_list_name: str


class Page(BaseModel):
    pageNumber: int
    pageUrl: str
    isCurrentPage: bool


class Pagination(BaseModel):
    summaryLabel: str
    pages: List[Page]


class SortItem(BaseModel):
    isSelected: bool
    value: str
    label: str


class Region(BaseModel):
    id: str
    name: str
    isSelected: bool
    indentLevel: int


class RegionList(BaseModel):
    regions: List[Region]
    regionType: str
    regionSingleText: str


class Display(BaseModel):
    showTripAdvisorReview: bool
    showStarRating: bool
    showMap: bool
    showMapOpenByDefault: bool


class Hotel(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
    image: str
    reviewImageUrl: str
    reviewTotals: str
    address: str
    city: str
    state: str
    postalCode: str
    country: str
    rateUnformatted: int
    rate: str
    rating: float
    isSaleable: bool


class Pois(BaseModel):
    class_: str = Field(..., alias='class')
    name: str
    id: int
    latitude: float
    longitude: float
    markerUrl: Union[bool, str]


class Map(BaseModel):
    hotels: List[Hotel]
    pois: List[Pois]
    defaultAttraction: Any


class Review(BaseModel):
    rating: str
    ratingUrl: str
    totalNumberOfReviews: str


class Display1(BaseModel):
    showPropertyContactInfo: bool
    showTripAdvisorReview: bool
    showStarRating: bool
    showPackages: bool
    showTopPick: bool
    showPriceDrop: bool
    showBlankRate: bool
    showRate: bool
    showSoldOutMessage: bool
    showSoldOutMessageAsLink: bool
    showCallToActionButton: bool
    showSelectDatesMessage: bool


class Price(BaseModel):
    undiscountedTeaserRate: Any
    teaserRate: str


class Urls(BaseModel):
    hotelSingleUrl: str
    hotelPackageUrl: str
    primaryCallToActionUrl: str


class GaListItemData(BaseModel):
    item_id: str
    item_name: str
    item_category: str
    index: int


class SourceSet(BaseModel):
    sourceSet: str
    media: str


class Image(BaseModel):
    sourceSets: List[SourceSet]
    url: str
    caption: str


class MarketingTextItem(BaseModel):
    isCallOut: bool
    promoText: str
    detailedText: str


class Hotel1(BaseModel):
    hotelId: int
    name: str
    city: str
    state: str
    phone: str
    website: str
    starRating: float
    pStarRating: str
    mStarRating: str
    review: Review
    hasPackages: bool
    distanceDescription: Any
    display: Display1
    price: Price
    urls: Urls
    gaListItemData: GaListItemData
    hotelDealBannerText: str
    image: Image
    marketingText: List[MarketingTextItem]
    soldOutMessage: str
    callToActionMessage: str


class Model(BaseModel):
    gaListData: GaListData
    pagination: Pagination
    sort: List[SortItem]
    regionList: RegionList
    display: Display
    map: Map
    searchParams: str
    hotels: List[Hotel1]