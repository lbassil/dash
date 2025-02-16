import pandas as pd

import plotly.express as px

from . import data, years
from .base_page import get_base_layout

indicators_dict = {
    "VIOLENCE": {
        "NAME": "Violence against Children and Women",
        "CARDS": [
            # revise denominator population: children 1-14?
            {
                "name": "who experienced physical punishment or psychological aggression by caregivers",
                "indicator": "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "denominator": "EDUNF_SAP_L1T3",
                "suffix": "Percent of Children",
            },
        ],
        "MAIN": {
            "name": "Violence and Harmful Practices",
            "geo": "Geographic area",
            "options": dict(
                lat="latitude",
                lon="longitude",
                size="OBS_VALUE",
                text="Geographic area",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.GnBu,
                size_max=40,
                zoom=2.5,
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
                "PT_F_GE15_SX_V_PTNR_12MNTH",
                "PT_VC_VOV_PHYL",
                "PT_VC_VOV_SEXL",
                "PT_VC_VOV_ROBB",
                "PT_VC_SNS_WALN",
                "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "PT_F_18-29_SX-V_AGE-18",
                "PT_M_18-29_SX-V_AGE-18",
                "PT_VC_PRR_PHYV",
                "PT_VC_PRR_SEXV",
                "PT_VC_PRR_ROBB",
                "PT_ADLT_PS_NEC",
                "PT_F_15-49_W-BTNG",
                "PT_M_15-49_W-BTNG",
                "PT_ST_13-15_BUL_30-DYS",
                "PT_F_15-19_MRD",
                "PT_M_15-19_MRD",
                "PT_F_20-24_MRD_U15",
                "PT_F_20-24_MRD_U18",
                "PT_M_20-24_MRD_U18",
                "PT_CHLD_5-17_LBR_ECON",
                "PT_CHLD_5-17_LBR_ECON-HC",
            ],
            "default": "PT_CHLD_1-14_PS-PSY-V_CGVR",
        },
        "AREA_1": {
            "type": "bar",
            "options": dict(
                x="Geographic area", y="OBS_VALUE", barmode="group", text="TIME_PERIOD",
            ),
            "compare": "Sex",
            "indicators": [
                "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
                "PT_F_GE15_SX_V_PTNR_12MNTH",
                "PT_VC_VOV_PHYL",
                "PT_VC_VOV_SEXL",
                "PT_VC_VOV_ROBB",
                "PT_VC_SNS_WALN",
                "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "PT_F_18-29_SX-V_AGE-18",
                "PT_M_18-29_SX-V_AGE-18",
                "PT_VC_PRR_PHYV",
                "PT_VC_PRR_SEXV",
                "PT_VC_PRR_ROBB",
                "PT_ADLT_PS_NEC",
                "PT_F_15-49_W-BTNG",
                "PT_M_15-49_W-BTNG",
                "PT_ST_13-15_BUL_30-DYS",
                "PT_F_15-19_MRD",
                "PT_M_15-19_MRD",
                "PT_F_20-24_MRD_U15",
                "PT_F_20-24_MRD_U18",
                "PT_M_20-24_MRD_U18",
                "PT_CHLD_5-17_LBR_ECON",
                "PT_CHLD_5-17_LBR_ECON-HC",
            ],
            "default": "PT_CHLD_1-14_PS-PSY-V_CGVR",
        },
        "AREA_2": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        text="TIME_PERIOD",
                    ),
                    "compare": "Sex",
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Geographic area",
                        hover_name="Geographic area",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "indicators": [
                "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
                "PT_F_GE15_SX_V_PTNR_12MNTH",
                "PT_VC_VOV_PHYL",
                "PT_VC_VOV_SEXL",
                "PT_VC_VOV_ROBB",
                "PT_VC_SNS_WALN",
                "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "PT_F_18-29_SX-V_AGE-18",
                "PT_M_18-29_SX-V_AGE-18",
                "PT_VC_PRR_PHYV",
                "PT_VC_PRR_SEXV",
                "PT_VC_PRR_ROBB",
                "PT_ADLT_PS_NEC",
                "PT_F_15-49_W-BTNG",
                "PT_M_15-49_W-BTNG",
                "PT_ST_13-15_BUL_30-DYS",
                "PT_F_15-19_MRD",
                "PT_M_15-19_MRD",
                "PT_F_20-24_MRD_U15",
                "PT_F_20-24_MRD_U18",
                "PT_M_20-24_MRD_U18",
                "PT_CHLD_5-17_LBR_ECON",
                "PT_CHLD_5-17_LBR_ECON-HC",
            ],
            "default_graph": "line",
            "default": "PT_CHLD_1-14_PS-PSY-V_CGVR",
        },
    },
    "CARE": {
        "NAME": "Children without parental care",
        "CARDS": [
            {
                "name": "in Residential Care",
                "indicator": "PT_CHLD_INRESIDENTIAL",
                "suffix": "Children",
            },
            # revise denominator: population children 0-17
            {
                "name": "in Residential Care",
                "indicator": "PT_CHLD_INRESIDENTIAL_RATE_B",
                "denominator": "EDUNF_SAP_L1T3",
                "suffix": "Percent of Children",
            },
            {
                "name": "in care of foster parents or guardians",
                "indicator": "PT_CHLD_INCARE_FOSTER",
                "suffix": "Children",
            },
            {
                "name": "available for adoption",
                "indicator": "PT_CHLD_ADOPTION_AVAILABLE",
                "suffix": "Children",
            },
        ],
        "MAIN": {
            "name": "Children without parental care",
            "geo": "Geographic area",
            "options": dict(
                lat="latitude",
                lon="longitude",
                size="OBS_VALUE",
                text="Geographic area",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.GnBu,
                size_max=40,
                zoom=2.5,
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "PT_CHLD_INRESIDENTIAL",
                "PT_CHLD_INRESIDENTIAL_RATE_B",
                "PT_CHLD_DISAB_PUBLIC",
                "PT_CHLD_LEFTRESCARE",
                "PT_CHLD_LEFTRESCARE_RETURNED",
                "PT_CHLD_LEFTRESCARE_INFAMILY",
                "PT_CHLD_LEFTRESCARE_ADOPTED",
                "PT_CHLD_LEFTRESCARE_INDEPENDENT",
                "PT_CHLD_LEFTRESCARE_TRANSFERED",
                "PT_CHLD_LEFTRESCARE_DIED",
                "PT_CHLD_LEFTRESCARE_OTHER",
                "PT_CHLD_CARED_BY_FOSTER",
                "PT_CHLD_CARED_BY_FOSTER_RATE",
                "PT_CHLD_DISAB_FOSTER",
                "PT_CHLD_CARED_GUARDIAN",
                "PT_CHLD_CARED_GUARDIAN_RATE",
                "PT_CHLD_DISAB_CARED_GUARDIAN",
                "PT_CHLD_GUARDIAN",
                "PT_CHLD_ENTEREDFOSTER",
                "PT_CHLD_ADOPTION_RATE",
                "PT_CHLD_ADOPTION",
                "PT_CHLD_ADOPTION_DISAB",
                "PT_CHLD_ADOPTION_AVAILABLE",
                "PT_CHLD_ADOPTION_AVAILABLE_DISAB",
            ],
        },
        "AREA_1": {
            "type": "bar",
            "options": dict(
                x="Geographic area", y="OBS_VALUE", barmode="group", text="TIME_PERIOD",
            ),
            # compare is the default selection
            "compare": "Sex",
            "default": "PT_CHLD_INRESIDENTIAL",
            "indicators": [
                "PT_CHLD_INRESIDENTIAL",
                "PT_CHLD_INRESIDENTIAL_RATE_B",
                "PT_CHLD_DISAB_PUBLIC",
                "PT_CHLD_LEFTRESCARE",
                "PT_CHLD_LEFTRESCARE_RETURNED",
                "PT_CHLD_LEFTRESCARE_INFAMILY",
                "PT_CHLD_LEFTRESCARE_ADOPTED",
                "PT_CHLD_LEFTRESCARE_INDEPENDENT",
                "PT_CHLD_LEFTRESCARE_TRANSFERED",
                "PT_CHLD_LEFTRESCARE_DIED",
                "PT_CHLD_LEFTRESCARE_OTHER",
                "PT_CHLD_CARED_BY_FOSTER",
                "PT_CHLD_CARED_BY_FOSTER_RATE",
                "PT_CHLD_DISAB_FOSTER",
                "PT_CHLD_CARED_GUARDIAN",
                "PT_CHLD_CARED_GUARDIAN_RATE",
                "PT_CHLD_DISAB_CARED_GUARDIAN",
                "PT_CHLD_GUARDIAN",
                "PT_CHLD_ENTEREDFOSTER",
                "PT_CHLD_ADOPTION_RATE",
                "PT_CHLD_ADOPTION",
                "PT_CHLD_ADOPTION_DISAB",
                "PT_CHLD_ADOPTION_AVAILABLE",
                "PT_CHLD_ADOPTION_AVAILABLE_DISAB",
            ],
        },
        "AREA_2": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        text="TIME_PERIOD",
                    ),
                    "compare": "Sex",
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Geographic area",
                        hover_name="Geographic area",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "indicators": [
                "PT_CHLD_INRESIDENTIAL",
                "PT_CHLD_INRESIDENTIAL_RATE_B",
                "PT_CHLD_DISAB_PUBLIC",
                "PT_CHLD_LEFTRESCARE",
                "PT_CHLD_LEFTRESCARE_RETURNED",
                "PT_CHLD_LEFTRESCARE_INFAMILY",
                "PT_CHLD_LEFTRESCARE_ADOPTED",
                "PT_CHLD_LEFTRESCARE_INDEPENDENT",
                "PT_CHLD_LEFTRESCARE_TRANSFERED",
                "PT_CHLD_LEFTRESCARE_DIED",
                "PT_CHLD_LEFTRESCARE_OTHER",
                "PT_CHLD_CARED_BY_FOSTER",
                "PT_CHLD_CARED_BY_FOSTER_RATE",
                "PT_CHLD_DISAB_FOSTER",
                "PT_CHLD_CARED_GUARDIAN",
                "PT_CHLD_CARED_GUARDIAN_RATE",
                "PT_CHLD_DISAB_CARED_GUARDIAN",
                "PT_CHLD_GUARDIAN",
                "PT_CHLD_ENTEREDFOSTER",
                "PT_CHLD_ADOPTION_RATE",
                "PT_CHLD_ADOPTION",
                "PT_CHLD_ADOPTION_DISAB",
                "PT_CHLD_ADOPTION_AVAILABLE",
                "PT_CHLD_ADOPTION_AVAILABLE_DISAB",
            ],
            "default_graph": "line",
            "default": "PT_CHLD_INRESIDENTIAL",
        },
    },
    "JUSTICE": {
        "NAME": "Access to Justice",
        "CARDS": [
            {
                "name": "committed against children during the year",
                "indicator": "JJ_CHLD_CRIME",
                "suffix": "Registered crimes",
            },
            {
                "name": "who are reported as being in contact with the police because of their own behaviour during the year",
                "indicator": "JJ_CHLD_POLICE",
                "suffix": "Children",
            },
            {
                "name": "who are charged with an offence or crime during the year",
                "indicator": "JJ_CHLD_OFFENCE",
                "suffix": "Children",
            },
            # revise denominator: population children 0-17
            # we don't have the ability yet to deal with rates that are not percentage
            # {
            #     "name": "committed against children (per 100,000 population aged 0-17)",
            #     "indicator": "JJ_CHLD_CRIMERT",
            #     "denominator": "EDUNF_SAP_L1T3",
            #     "suffix": "Registered crimes",
            # },
            # revise denominator: population children 14-17
            # we don't have the ability yet to deal with rates that are not percentage
            # {
            #     "name": "who are sentenced (per 100,000 population aged 14-17)",
            #     "indicator": "JJ_CHLD_SENTENCERT",
            #     "denominator": "EDUNF_SAP_L3",
            #     "suffix": "Children",
            # },
        ],
        "MAIN": {
            "name": "Child Victims of Crime",
            "geo": "Geographic area",
            "options": dict(
                lat="latitude",
                lon="longitude",
                size="OBS_VALUE",
                text="Geographic area",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.GnBu,
                size_max=40,
                zoom=2.5,
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "JJ_CHLD_CRIME",
                "JJ_CHLD_CRIMERT",
                "JJ_CHLD_DETENTION",
                "JJ_CHLD_CONVICTED",
                "JJ_CHLD_SENTENCERT",
                "JJ_VC_PRS_UNSNT",
            ],
            "default": "JJ_CHLD_CRIME",
        },
        "AREA_1": {
            "type": "bar",
            "options": dict(
                x="Geographic area", y="OBS_VALUE", barmode="group", text="TIME_PERIOD",
            ),
            "compare": "Sex",
            "indicators": [
                "JJ_CHLD_CRIME",
                "JJ_CHLD_CRIMERT",
                "JJ_CHLD_DETENTION",
                "JJ_CHLD_CONVICTED",
                "JJ_CHLD_SENTENCERT",
                "JJ_VC_PRS_UNSNT",
            ],
            "default": "JJ_CHLD_CRIME",
        },
        "AREA_2": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        text="TIME_PERIOD",
                    ),
                    "compare": "Sex",
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Geographic area",
                        hover_name="Geographic area",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "indicators": [
                "JJ_CHLD_CRIME",
                "JJ_CHLD_CRIMERT",
                "JJ_CHLD_DETENTION",
                "JJ_CHLD_CONVICTED",
                "JJ_CHLD_SENTENCERT",
                "JJ_VC_PRS_UNSNT",
            ],
            "default_graph": "line",
            "default": "JJ_CHLD_CRIME",
        },
    },
}


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    return get_base_layout(**kwargs)
